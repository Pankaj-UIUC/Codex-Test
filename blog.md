---
layout: page
title: Blog
permalink: /blog/
---

Catch up on the latest posts from my work in data science and analytics.

Connect with me on [LinkedIn](https://www.linkedin.com/in/psharma13/) for more updates and professional insights.

<ul class="post-list">
  {%- for post in site.posts -%}
  <li>
    <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>
    <h3>
      <a class="post-link" href="{{ post.url | relative_url }}">
        {{ post.title | escape }}
      </a>
    </h3>
    {%- if post.excerpt -%}
    <p>{{ post.excerpt | strip_html | truncate: 160 }}</p>
    {%- endif -%}
  </li>
  {%- endfor -%}
</ul>
