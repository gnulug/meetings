- What problems does GPG/friends solve?
  - Certifying authorship of source code (git commit signing)
  - Certifying authenticity of packages for package managear
  - Private messages on public channel
    - E.g., emailing political dissidents
    - Less often, these days, due to e2e-encrypted messengers)
- What building blocks do we use to solve?
  - [Asymmetric crypto](https://en.wikipedia.org/wiki/Public-key_cryptography)
    - Very good paper: [New Directions in Cryptography by Diffie and Hellman (1976)](https://ee.stanford.edu/%7Ehellman/publications/24.pdf)
  - But now we need a way to get the public keys to you (PKI)
    - <https://xkcd.com/1181/>
    - Root CAs
      - [x.509](https://en.wikipedia.org/wiki/X.509) certifiate standard
      - HTTPS, DNSSEC
      - Con: centralized authority can censor, get hacked, charge money, get subpoena'ed ...
      - Self-signed certs
    - Trust-on-first-use (TOFU)
      - OpenSSH client strategy
      - Cons: doesn't secure first use
    - Web of trust (WoT)
      - Open standard: Pretty Good Privacy (OpenPGP)
      - Main implementation: Gnu Privacy Guard (GPG or GnuPG)
      - Decentralized, peer-to-peer
      - [stronk set](https://web.archive.org/web/20200621062831/https://pgp.cs.uu.nl/plot/)
      - Inherent cons:
        - [OpenPGP Certificate Flooding](https://dkg.fifthhorseman.net/blog/openpgp-certificate-flooding.html)
        - [Good paper](https://dl.acm.org/doi/pdf/10.1145/3524458.3548488)
        - [Long-term keys/no forward secrecy](https://www.latacora.com/blog/2019/07/16/the-pgp-problem/)
        - Leaks metadata on "who signs who"
        - How well did you verify their identity?
      - Implementation cons:
        - [The PGP problem](https://www.latacora.com/blog/2019/07/16/the-pgp-problem/)
        - Complex, swiss-army knife with footguns, bad UX
        - [No AEAD](https://security.stackexchange.com/questions/275883/should-one-really-disable-aead-for-recent-gnupg-created-pgp-keys)
        - [Follows UNIX philosophy](https://news.ycombinator.com/item?id=27431325) (therefore has to reparse the key database on every invocation)
        - Older, weaker crypto algos [CFB mode, RSA vs ED25519](https://www.latacora.com/blog/2019/07/16/the-pgp-problem/), [the defaults suck](https://blog.cryptographyengineering.com/2014/08/13/whats-matter-with-pgp/)
- Practical, how to
  - [gpg.wtf](https://gpg.wtf/), getting started guide to common use-cases
  - [GPG on ArchWiki](https://wiki.archlinux.org/title/GnuPG)
  - [GPG cheatsheet](https://gock.net/blog/2020/gpg-cheat-sheet)
  - GPG without WoT
    - [Keybase.io](https://keybase.io/)
    - [Keyoxide](https://keyoxide.org/)
      - [Web Key Directory](https://wiki.gnupg.org/WKD), put your SSH key at `www.{your-domain}.com/.well-known/openpgpkey/hu/{hash(email)}`
- GPG alternatives:
  - Never encypt email [efail](https://efail.de/), quote replies, nobody knows how to use it anyway.
  - Sending files: [Magic Wormhole](https://magic-wormhole.readthedocs.io/en/latest/) (point-to-point, synchronous)
  - Signing: [minisign](https://jedisct1.github.io/minisign/), [signify](https://man.openbsd.org/signify)
    - Use [SSH keys to sign Git commits](https://docs.gitlab.com/user/project/repository/signed_commits/ssh/)
    - How to get publisher's public key? What does SSH signing get you?
    - ~~[sigstore](https://www.sigstore.dev/)~~
      - It's kind of hard to decrypt the Big Tech, Venture Cap, B2B, synergy langauge they use, but once I did, I found this:
      
        > The `cosign` command requests a certificate from the Sigstore certificate authority, Fulcio.
        > 
        > [_Cool; it hard-depends on a centralized service_]
        >
        > Note that you don’t need to use a key to sign. Currently, you can authenticate with Google, GitHub, or Microsoft, which will associate your identity with a short-lived signing key.
        >
        > [_Because those companies would never want to censor anyone, and everyone wants to tie their Google account to their digital identity._]
  - Encrypting files: [age](https://words.filippo.io/age-authentication/)
    - > age is in the business of integrity and confidentiality, not authentication. This was [hotly debated early on](https://github.com/FiloSottile/age/issues/51), and still is [periodically](https://twitter.com/FiloSottile/status/1475954548556673024)....
      >
      > In short, while no one can modify an encrypted age file, anyone can replace it with a completely new encrypted file.
      - remember, recepient's public keys are public
      - > `minisign`/`signify` - AFAIK the tools and their formats do not support streamed verification, thus they cannot simply be used together with age in command or library form in streaming use cases. It means requiring more storage/passes and opening for TOCTOU vulnerabilities. --- [GitHub issue 51 comment](https://github.com/FiloSottile/age/issues/51#issuecomment-569843004)
    - This comment on HN comes dangerously close to realizing why we had WoT in the first place.
        
      > > The big problem is there are no really good ways to deal with this problem [the switcharoo problem] fully.
      > If you use digital signatures, you have to have a trusted method of distributing the verification keys.
      >
      > If you have a secure method of distributing keys, you could also just distribute the encrypted file (or its hash) via that secure method.
      > --- [Hackernews comment](https://news.ycombinator.com/item?id=32998851)

      Of course, the last syllogism is false. A and B could have established a secure channel a long time ago, B and C (not necessarily afterwards), C and D, A can rececive D's key with authenticity, but there was never a secure channel from A to D directly.

  - E2e messaging:
    - [Matrix](https://matrix.org), requires always-online server
      - Could be used for more than just chat
    - [XMPP + OMEMO](https://xmpp.org/extensions/xep-0384.html)
      - Pre-existing chat protocol
    - [Signal](https://signal.org/) / OpenWhisper protocol
    - Basically, device-local keys (aka host keys) that sign each other on a server.
  - [Soatok's blog](https://soatok.blog/2024/11/15/what-to-use-instead-of-pgp/)
- Discussion questions:
  - The [Monkeysphere project](https://web.archive.org/web/20200119092843/https://monkeysphere.info/) lets you use GPG keys for users to authenticate to SSH/Web servers AND authenticate servers (the reverse). Is this a good idea?
  - Are decentralized protocols inherently slow-moving and thus incompatible with up-to-date-ness?
    - [The Ecosystem is Moving by Moxie Marlinspike of Signal (2016)](https://signal.org/blog/the-ecosystem-is-moving/)
    - [On Privacy versus Freedom by Matthew Hodgson of Matrix (2020)](https://matrix.org/blog/2020/01/02/on-privacy-versus-freedom/)
  - Is it even possible to get perfect forward secrecy for a static thing, without servers?
  - In [IndieWebAuth](https://indieweb.org/IndieAuth), you can authenticate to arbitary web services by proving you own a domain-name, no keys or passwords involved. When would this be sufficient, and when would you want something more?
    - Indeed BlueSky, while not implementing IndieWebAuth, lets you use a [verified domain name as your account name](https://bsky.social/about/blog/4-28-2023-domain-handle-tutorial).
    - Likewise, WKD and DNS-based Authentication of Named Entities (DANE) utilize DNS as a delegatable naming authority.
