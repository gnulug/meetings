import collections
import datetime
import enum
import itertools
import pathlib
import re
import warnings
import bs4
import marko
import yaml


class Semester(enum.IntEnum):
    # Needed for sorting, so SPRING < FALL
    SPRING = enum.auto()
    FALL = enum.auto()


def get_semester_dirs(root_dir: pathlib.Path) -> list[tuple[int, Semester, pathlib.Path]]:
    ret = []
    for semester_dir in root_dir.iterdir():
        if semester_dir.is_dir() and (match := re.match("([0-9]{4})([sf])", semester_dir.name)):
            year = int(match.group(1))
            semester = {"s": Semester.SPRING, "f": Semester.FALL}[match.group(2)]
            ret.append((year, semester, semester_dir))
    return ret


def get_event_dirs(
        semester_dir: pathlib.Path
) -> list[tuple[datetime.date, pathlib.Path]]:
    ret = []
    for event_dir in semester_dir.iterdir():
        if event_dir.is_dir():
            try:
                date = datetime.date.fromisoformat(event_dir.name)
            except ValueError:
                warnings.warn(f"Could not parse {event_dir.name}")
            else:
                ret.append((date, event_dir))
    return ret


def get_main_notes(event_dir: pathlib.Path) -> pathlib.Path | None:
    for notes in ["notes.yml", "notes.yaml", "notes.html", "README.md", "notes.md", "notes.txt", "writeup.md"]:
        if (event_dir / notes).exists():
            return event_dir / notes
    return None


def get_titles(notes: pathlib.Path) -> list[str] | None:
    if notes.suffix in get_titles_format:
        try:
            return get_titles_format[notes.suffix](notes.read_text())
        except Exception as exc:
            # Add the path we were trying to parse as context to the exception
            warnings.warn(f"Could not parse {notes}: {type(exc).__name__}: {str(exc)}")
    else:
        return None


def remove_tba(titles: collections.abc.Iterable[str]) -> list[str]:
    return [title for title in titles if title != "TBA"]


usages = collections.Counter()


def get_titles_yaml(source: str) -> list[str] | None:
    document = yaml.safe_load(source)
    if "title" in document:
        usages["yaml title"] += 1
        return [document["title"]]
    elif "Talks" in document:
        # We want document -> Talks -> Big Talks if exists, but will work with Talks otherwise.
        if isinstance(document["Talks"], dict) and "Big Talks" in document["Talks"]:
            usages["yaml talks -> big talks"] += 1
            talks = document["Talks"]["Big Talks"]
        elif isinstance(document["Talks"], (list, dict)):
            usages["yaml talks -> talks"] += 1
            talks = document["Talks"]
        else:
            warnings.warn("document['Talks'] is not a list or dict")
            return None

        # Gotten talks.
        if isinstance(talks, list) and all(isinstance(talk, str) for talk in talks):
            usages["yaml talks list[str]"] += 1
            return remove_tba(talks)
        elif isinstance(talks, dict):
            if isinstance(talks.get("Title"), list):
                usages["yaml talks list[dict]"] += 1
                return remove_tba(talks["Title"])
            else:
                usages["yaml talks dict"] += 1
                return remove_tba(talks.keys())
        else:
            warnings.warn("document['Talks']['Big Talks'] or document['Talks'] is an unknown datatype")
            return None
    else:
        warnings.warn("Could not find 'Talks' or 'title'")
        return None


markdown = marko.Markdown()


def get_titles_markdown(source: str) -> list[str] | None:
    fence = "---\n"
    if source.startswith(fence) and source.count(fence) >= 2:
        usages["markdown yaml fence"] += 1
        fence_index = source.index(fence, len(fence))
        return get_titles_yaml(source[:fence_index])
    else:
        usages["markdown headings"] += 1
        return [
            " ".join(
                grandchild.children
                for grandchild in child.children
                if isinstance(grandchild, marko.inline.RawText)
            )
            for child in markdown.parse(source).children
            if isinstance(child, marko.block.Heading) and child.level == 1
        ]


def get_titles_txt(source: str) -> list[str] | None:
    usages["txt"] += 1
    return None

        
def get_titles_html(source: str) -> list[str] | None:
    usages["html title"] += 1
    soup = bs4.BeautifulSoup(source)
    return list(soup.find("title"))[0].text


get_titles_format = {
    ".yaml": get_titles_yaml,
    ".yml": get_titles_yaml,
    ".md": get_titles_markdown,
    ".txt": get_titles_txt,
    ".html": get_titles_html,
}


def replace_autogen_section(
        source: str,
        begin_autogen_tag: str,
        end_autogen_tag: str,
        autogen_body: str,
) -> str:
    begin_autogen_idx = source.index(begin_autogen_tag) + len(begin_autogen_tag)
    end_autogen_idx = source.index(end_autogen_tag, begin_autogen_idx)
    return source[:begin_autogen_idx] + autogen_body + source[end_autogen_idx:]


if __name__ == "__main__":
    root_dir = pathlib.Path()
    no_title_found = []
    autogen_markdown = []
    semester_dirs = sorted(get_semester_dirs(root_dir), reverse=True)
    for year, semester, semester_dir in semester_dirs:
        autogen_markdown.append(f"# {year} {semester.name.lower().capitalize()}")
        semester_links = []
        for date, event_dir in sorted(get_event_dirs(semester_dir), reverse=True):
            main_notes = get_main_notes(event_dir)
            if main_notes is not None:
                titles = get_titles(main_notes)
                if titles is not None:
                    for title in titles:
                        semester_links.append(f"- [{title}](./{main_notes})")
                else:
                    no_title_found.append(main_notes)                
        autogen_markdown.extend(semester_links)

    readme_path = root_dir / "README.md"
    readme_path.write_text(
        replace_autogen_section(
            readme_path.read_text(),
            "\n<!-- BEGIN_AUTOGEN -->\n",
            "\n<!-- END_AUTOGEN -->\n",
            "\n".join(autogen_markdown)
        )
    )


    print("\n\nNo title found:")
    for file in no_title_found:
        print(file)

    print("\n\nUsage counts:")
    for usage, count in usages.most_common():
        print(count, usage)
