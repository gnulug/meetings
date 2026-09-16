Licensing Software in the Open

&nbsp;

- "Possession is 9/10ths of the law." \- A pearl of legal wisdom

&nbsp;

[The Open Source Definition by the Open Source Initiative](https://opensource.org/osd)

- Generally accepted (but not legally binding) definition of "open source"  
- In plain language, "open source" licenses require:  
  - The cost of a license be zero.  
  - The source be available.  
  - The equal (i.e non-discriminatory) treatment of users, including based on the intended use of the source.  
  - The end-users have the right to modify the source.

[Licenses which are popular or have a strong community per the Open Source Initiative](https://opensource.org/licenses?categories=popular-strong-community)

- A detailed table comparing a popular selection of these is found in the slide show.  
  - Of trivial note, the NCSA/University of Illinois license is not considered current.

  &nbsp;

Case Study

[Tandemn Labs](https://github.com/tandemn-labs#open-source)

- A startup with a GitHub Organization, employees, and public GitHub repositories  
- Quan Hao Ng, Founding Engineer at Tandemn and former GLUG President  
- Per the company's [README.md](https://github.com/tandemn-labs#open-source), Tandemn's software is "fully open source"

&nbsp;

Per US Copyright Law, works without a license (or a malformed e.g. contradictory licensing statement) remain the sole right of the creator or copyright holder i.e. the copyright holder reserves all rights or "All Rights Reserved."

&nbsp;

According to GitHub's Terms of Service (specifically [Section D.5](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service#5-license-grant-to-other-users)), making a repository public does grant other GitHub users limited rights to the repository's code viz. viewing the code on GitHub, forking the code via the GitHub UI. GitHub's ToS then rightfully and helpfully encourages users to [adopt a license](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository#including-an-open-source-license-in-your-repository).

&nbsp;

Problematic Projects

- Tandemn Docs \- [GitHub \- Tandemn Docs](https://github.com/Tandemn-Labs/Tandemn-docs)  
  - Unlicensed  
  - The documentation leads to the following repository  
- Tandemn System : [GitHub \- Tandemn System](https://github.com/Tandemn-Labs/tandemn-system/)  
  - Licensed\!  
  - Contains a git submodule to LLM\_Placement\_Solver, which is [unlicensed](https://github.com/Tandemn-Labs/LLM_placement_solver)  
    - As this is ambiguous, I would err on the side of saying this is a malformed licensing statement ergo All Rights Reserved (by Tandemn Labs) and therefore *not* open source.  
- Tandemn System : [GitHub \- tandemn-vllm](https://github.com/Tandemn-Labs/tandemn-vllm)  
  - Unlicensed  
  - Has contributions from both employees of Tandemn Labs (e.g. GitHub user orangeng) and outside contributors i.e. not employees of Tandemn  
  - Due to the lack of any explicit contributor guidelines, the employee contributions remain under the company's license, but outside contributor's contributions also remain under their exclusive license.  
  - As a result, the public code contains two sections of code, each licensed to different mutually-exclusive parties.  
  - In an extreme hypothetical, should Tandemn Labs deploy an outside contribution for monetary gain, the outside contributor could seek monetary compensation because their code (which they retain the rights to) was a part of the repository.

&nbsp;

Final thought

- License your code, hopefully with an open-source license.

&nbsp;

&nbsp;

&nbsp;