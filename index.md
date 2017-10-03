---
layout: default
title: MATE
---

It is important to make mobile apps accessible, so as not to exclude
users with common disabilities such as blindness, low vision, or color
blindness. Even when developers are aware of these accessibility
needs, the lack of tool support makes the development and assessment
of accessible apps challenging. Some properties can be checked
statically, but user interface widgets are often created dynamically
and are not amenable to static checking. Accessibility checking
frameworks analyze accessibility properties at runtime, but rely on
existing thorough test suites.


MATE automatically explores apps while applying different checks for
accessibility issues related to visual impairment. MATE generates a
test case that supports the developer in fixing the issue.
Experiments on a sample of apps demonstrate that MATE detects 52% more
basic accessibility problems than static analysis, and many additional
types of accessibility problems that cannot be detected statically at
all.


<div class="apps-list" id="apps-list">
  <input class="search" placeholder="Search" />
  <button class="sort" data-sort="name">Sort by name</button>
  <button class="sort" data-sort="flaws">Sort by # of flaws</button>

  <ul class="list">
    {% for post in site.posts %}
    <li class="app">
        <img src="{{ post.icon }}" class="avatar">
        <h4 class="name">{{ post.title }}</h4>
        <p class="summary">{{ post.summary }}</p>
        <a class="flaws" href="{{ post.report }}">{{ post.nflaws }} accessibility flaws</a>
    </li>
    {% endfor %}
  </ul>

</div>

<script>
var options = {
    valueNames: [ 'name', 'summary', 'flaws' ]
};

var hackerList = new List('apps-list', options);
</script>
