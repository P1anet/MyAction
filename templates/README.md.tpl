### Hi there 👋

🎓 Received a bachelor's degree from [College of Electrical Engineering, Zhejiang University](http://ee.zju.edu.cn/), and currently studing for a master's degree in [College of Computer Science and Technology, Zhejiang University](http://www.cs.zju.edu.cn/)

💻 Interested in machine learning and processing in memory.


#### 👷 Check out what I'm currently working on
{{range recentContributions 5}}
- [{{.Repo.Name}}]({{.Repo.URL}}) - {{.Repo.Description}} ({{humanize .OccurredAt}})
{{- end}}

#### 🌱 Check out my latest commits
{{range recentRepos 5}}
- [{{.Name}}]({{.URL}}) - {{.Description}}
{{- end}}

#### 🍴 Check out my recent forks
{{range recentForks 5}}
- [{{.Name}}]({{.URL}}) - {{.Description}}
{{- end}}

#### ⭐ Check out my recent stars
{{range recentStars 5}}
- [{{.Repo.Name}}]({{.Repo.URL}}) - {{.Repo.Description}} ({{humanize .StarredAt}})
{{- end}}

#### 👯 Check out my recent followers
{{range followers 5}}
- [{{.Login}}]({{.URL}})
{{- end}}

#### 📜 Check out my recent blog posts
{{range rss "https://p1anet.github.io/index.html" 5}}
- [{{.Title}}]({{.URL}}) ({{humanize .PublishedAt}})
{{- end}}

#### 💬 Feedback

Say Hello, I don't bite!

#### 📫 How to reach me

🖋 Blog：[Kenshin Blog](https://https://p1anet.github.io/) --- to be reconstructed

💡 Notion：[Personal Home](https://www.notion.so/Personal-Home-ce2fa1062dae41cc8f56525b5be3c23a?pvs=4) --- to be archived

📫 Email: [zjxin@zju.edu.cn](zjxin@zju.edu.cn)

💬 Wechat: [View QR code in issue #1](https://github.com/P1anet/P1anet/issues/1)



<!--
**P1anet/P1anet** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->

<!--
<picture>
  <source
    media="(prefers-color-scheme: dark)"
    srcset="
      https://api.star-history.com/svg?repos=star-history/star-history&type=Date&theme=dark
    "
  />
  <source
    media="(prefers-color-scheme: light)"
    srcset="
      https://api.star-history.com/svg?repos=star-history/star-history&type=Date
    "
  />
  <img
    alt="Star History Chart"
    src="https://api.star-history.com/svg?repos=star-history/star-history&type=Date"
  />
</picture>
-->

<!--
#### 🔭 Latest releases I've contributed to
{{range recentReleases 10}}
- [{{.Name}}]({{.URL}}) ([{{.LastRelease.TagName}}]({{.LastRelease.URL}}), {{humanize .LastRelease.PublishedAt}}) - {{.Description}}
{{- end}}

#### 🔨 My recent Pull Requests
{{range recentPullRequests 10}}
- [{{.Title}}]({{.URL}}) on [{{.Repo.Name}}]({{.Repo.URL}}) ({{humanize .CreatedAt}})
{{- end}}

#### 📓 Gists I wrote
{{range gists 5}}
- [{{.Description}}]({{.URL}}) ({{humanize .CreatedAt}})
{{- end}}

#### ❤️ These awesome people sponsor me (thank you!)
{{range sponsors 5}}
- [{{.User.Login}}]({{.User.URL}}) ({{humanize .CreatedAt}})
{{- end}}

#### 👯 Check out some of my recent followers
{{range followers 5}}
- [{{.Login}}]({{.URL}})
{{- end}}
-->