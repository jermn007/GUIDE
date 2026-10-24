# Privacy

Effective October 24, 2026.

This policy covers GUIDE: the Claude plugin, the Claude skill, and the Python library in this repository. GUIDE is an open-source project maintained by Jeremy Terhune. It is not a hosted service.

## The plugin and skill

The GUIDE plugin and skill contain only Markdown and JSON files: rubrics, instructions, and agent definitions. They have no code that runs, no hooks, and no MCP servers. They do not collect, store, or send any data, and they add no tracking or analytics.

When you use GUIDE in Claude, the content you share is part of your Claude conversation. Anthropic handles it under its own terms and [privacy policy](https://www.anthropic.com/legal/privacy). The GUIDE author does not receive your content.

If you install GUIDE from Anthropic's plugin directory, Anthropic shows the author usage figures for the listing: installs, versions, how often each skill runs, and error rates.

## The Python library

If you run the Python judges in this repository, your content goes from your own computer to the Anthropic API using your own API key, and to LangSmith if you choose to use it. Those services' own policies apply. The GUIDE author does not receive your content.

## GitHub

If you open an issue or contribute to this repository, what you post is public on GitHub, and [GitHub's privacy statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement) applies.

## Changes and questions

Changes to this policy are recorded in this file's history on GitHub. For questions, [open an issue](https://github.com/jermn007/GUIDE/issues).
