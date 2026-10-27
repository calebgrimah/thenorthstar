---
layout: home
title: Caleb Grimah — Software Engineer
description: Senior software engineer building mobile, web, backend, and connected-TV products. Explore selected work and engineering notes.
---
<section class="home-intro" id="me" aria-labelledby="intro-title">
  <div class="intro-heading">
    {% include portrait.html %}
    <div>
      <h1 id="intro-title">Caleb Grimah.</h1>
      <p class="intro-role">Senior software engineer.</p>
      <p class="intro-location">Abuja, Nigeria · Working across platforms</p>
    </div>
  </div>
  <p class="intro-description">I build complete products — from the interface in your hand to the services behind it. My work spans streaming, healthcare, and business software across mobile, web, and connected TV. I’m currently building Astera for creator campaigns and Omari for everyday business operations.</p>
  <div class="intro-actions">
    <a class="primary-link" href="#work">Explore my work <span aria-hidden="true">↓</span></a>
    <a href="{{ '/assets/docs/CalebGrimahMainRobustResume.pdf' | relative_url }}">Resume</a>
  </div>
</section>

<section class="home-work" id="work" aria-labelledby="work-title">
  <div class="section-heading">
    <h2 id="work-title">Notable projects</h2>
    <a href="{{ '/calebgrimah/' | relative_url }}">Full portfolio <span aria-hidden="true">↗</span></a>
  </div>
  <p class="section-intro">Products I’m building, and the platforms I’ve helped bring to life.</p>
  {% for project in site.data.featured_projects %}
  <article class="work-entry work-entry--{{ project.id }}">
    <h3><a href="{{ '/calebgrimah/' | relative_url }}#{{ project.id }}">{{ project.title }} <span aria-hidden="true">↗</span></a></h3>
    {% include project_media.html project=project %}
    <p>{{ project.summary }}</p>
    <p class="work-stack">{{ project.stack }}</p>
    <a class="work-details" href="{{ '/calebgrimah/' | relative_url }}#{{ project.id }}">Project details<span class="sr-only">: {{ project.title }}</span></a>
  </article>
  {% endfor %}
  <h3 class="more-work-title">More production work</h3>
  <article class="work-entry">
    <h3><a href="https://www.endeavorstreaming.com/platform/">Vesper Streaming Platform <span aria-hidden="true">↗</span></a></h3>
    <p>At Endeavor Streaming, I build reusable product features across mobile, web, and connected TV, adapting navigation and performance to each screen and input model.</p>
    <p class="work-stack">React Native / React / TypeScript</p>
  </article>
  <article class="work-entry">
    <h3><a href="https://getcare.eha.ng/">Healthcare at eHealth Africa <span aria-hidden="true">↗</span></a></h3>
    <p>At eHealth Africa, I worked across patient applications, healthcare operations, and backend services — connecting appointments, medical records, payments, and care.</p>
    <p class="work-stack">Mobile / Web / Backend services</p>
  </article>
  <article class="work-entry">
    <h3><a href="{{ '/calebgrimah/' | relative_url }}">Udongo · Offline-first Android <span aria-hidden="true">↗</span></a></h3>
    <p>An offline-first Android application for agricultural extension agents. Local persistence and background synchronization keep core workflows available when the network isn’t.</p>
    <p class="work-stack">Android / Local persistence / Sync</p>
  </article>
</section>

<section class="home-practice" aria-labelledby="practice-title">
  <h2 id="practice-title">How I build.</h2>
  <div>
    <p>Different screens. Unreliable networks. Devices with limited resources. I care about the details that make software useful beyond the development environment.</p>
    <p>My work connects React Native, React, and native Android interfaces with Node.js and Spring Boot services. Alongside implementation, I contribute through code review, performance diagnosis, and technical mentoring.</p>
    <a href="{{ '/calebgrimah/' | relative_url }}">More about my experience <span aria-hidden="true">↗</span></a>
  </div>
</section>

<section class="home-notes" aria-labelledby="notes-title">
  <div class="section-heading">
    <h2 id="notes-title">Notes & ideas</h2>
    <a href="{{ '/journal/' | relative_url }}">Visit the journal <span aria-hidden="true">↗</span></a>
  </div>
  <p>A quieter corner for thoughts, experiments, and things I’m learning.</p>
  <ul class="recent-notes">
    {% for post in site.posts limit: 2 %}
    <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a><time datetime="{{ post.date | date: '%Y-%m-%d' }}">{{ post.date | date: '%b %Y' }}</time></li>
    {% endfor %}
  </ul>
</section>

<section class="home-contact" aria-labelledby="contact-title">
  <h2 id="contact-title">Have something in mind?</h2>
  <p>For engineering conversations, collaborations, or a simple hello.</p>
  <div class="contact-emails">
    <a class="contact-email" href="mailto:caleb.grimah@gmail.com">caleb.grimah@gmail.com</a>
    <a class="contact-email" href="mailto:caleb.grimah@arcadereality.org">caleb.grimah@arcadereality.org</a>
  </div>
  <div class="social-links">
    <a href="https://github.com/calebgrimah">GitHub <span aria-hidden="true">↗</span></a>
    <a href="https://www.linkedin.com/in/caleb-grimah-8678aa122/">LinkedIn <span aria-hidden="true">↗</span></a>
  </div>
</section>
