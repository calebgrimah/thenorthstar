---
layout: page
title: Caleb Grimah
permalink: /calebgrimah/
description: Senior Software Engineer specializing in full-stack product engineering, React Native, Android, web, backend services, and connected-TV applications.
---

<section class="profile-hero">
  {% include portrait.html %}
  <div>
    <h2>Software that works across platforms.</h2>
    <p>
      I build production software across mobile, web, backend, and large-screen platforms. My work spans streaming products used by millions, healthcare systems, e-commerce workflows, offline-first Android applications, and full-stack business tools.
    </p>
    <p class="profile-actions">
      <a href="mailto:caleb.grimah@gmail.com">Email</a>
      <a href="mailto:caleb.grimah@arcadereality.org">Alternate Email</a>
      <a href="https://github.com/calebgrimah">GitHub</a>
      <a href="https://www.linkedin.com/in/caleb-grimah-8678aa122/">LinkedIn</a>
      <a href="{{ '/assets/docs/caleb-grimah-resume.pdf' | relative_url }}">Resume</a>
    </p>
  </div>
</section>

<nav class="profile-section-nav" aria-label="On this page">
  <a href="#notable-projects">Notable projects</a>
  <a href="#experience">Experience</a>
  <a href="#technical-focus">Technical focus</a>
  <a href="#contact">Contact</a>
</nav>

## Notable projects {#notable-projects}

<div class="portfolio-grid">
  {% for project in site.data.featured_projects %}
    {% include project_detail.html project=project %}
  {% endfor %}

  <article>
    <h3>Vesper Streaming Platform</h3>
    <p class="project-meta">Endeavor Streaming / React Native, React, JavaScript, TypeScript, web, mobile, connected TV</p>
    <p>Vesper is Endeavor Streaming's platform for building and operating direct-to-consumer video experiences. My work includes reusable cross-platform features, large-screen interaction patterns, performance improvements, and production delivery across mobile, browser, and connected-TV environments.</p>
    <p><a href="https://www.endeavorstreaming.com/platform/">Explore Vesper</a></p>
  </article>

  <article>
    <h3>Health-Mate</h3>
    <p class="project-meta">eHealth Africa / EHA Clinics / React Native, mobile, REST APIs, Android, iOS</p>
    <p>Patient-facing mobile application supporting appointments, medical records, lab services, pharmaceutical ordering, health tracking, payments, and other digital healthcare workflows. I contributed mobile features, API integration, testing, debugging, and production maintenance.</p>
    <p><a href="https://play.google.com/store/apps/details?id=ng.eha.healthmate&amp;hl=en_GB">Health-Mate on Google Play</a> and <a href="https://erp.eha.ng/services/informatics">EHA Informatics</a></p>
  </article>

  <article>
    <h3>EHA Clinics Platform</h3>
    <p class="project-meta">eHealth Africa / React, JavaScript, TypeScript, Node.js, Express, REST APIs, databases</p>
    <p>Web and backend systems supporting patient-facing and internal healthcare operations. Work included responsive React interfaces, Node.js/Express services, REST APIs, data access, integration paths, and reliability improvements for healthcare workflows.</p>
    <p><a href="https://www.eha.care/">EHA Clinics</a> and <a href="https://erp.eha.ng/services/informatics">EHA Informatics</a></p>
  </article>

  <article>
    <h3>GetCare</h3>
    <p class="project-meta">EHA Clinics / web, mobile integration, backend services, REST APIs, transactional workflows</p>
    <p>Healthcare commerce and online-services platform for medication purchases, appointments, telehealth, frontend/backend integration, and transactional workflows. I worked across client and backend paths used by patients and operations teams.</p>
    <p><a href="https://getcare.eha.ng/">Explore GetCare</a></p>
  </article>

  <article>
    <h3>Udongo</h3>
    <p class="project-meta">Teal Technology Service / native Android, Kotlin, Java, offline-first architecture</p>
    <p>Android app for agricultural extension agents. I implemented offline-first workflows, local data management, API synchronization, Android UI features, compatibility improvements, testing, debugging, and performance work for constrained mobile devices.</p>
    <p><strong>Reference:</strong> Android package <code>ng.udongo.android</code></p>
  </article>

  <article>
    <h3>Biosec Business Applications</h3>
    <p class="project-meta">Biosec Solutions / JavaScript, Java, Python, HTML, CSS, databases</p>
    <p>Full-stack business applications for an identity-management and technology consultancy. I delivered features across UI, business logic, persistence, integration, testing, debugging, and release workflows.</p>
    <p><a href="https://biosec.com.ng/">Biosec Solutions</a></p>
  </article>
</div>


## Experience {#experience}

### Endeavor Streaming

**Senior Software Engineer, Endeavor Streaming**  
Remote, October 2024 - Present

Build and ship production streaming experiences across mobile, web, and connected-TV platforms, contributing to the Vesper direct-to-consumer video platform ecosystem.

- Build and maintain React Native and React applications using JavaScript and TypeScript across phones, browsers, and large-screen television environments.
- Develop reusable cross-platform components and features that adapt across device classes, screen sizes, input methods, navigation models, and performance constraints.
- Diagnose production issues and optimize application performance across devices with different processing power, memory capacity, rendering capabilities, and network conditions.
- Review production code and provide implementation feedback focused on correctness, maintainability, performance, architecture, and engineering best practices.
- Mentor junior engineers through code reviews, debugging sessions, technical guidance, implementation feedback, and knowledge sharing.
- Platform: [Vesper direct-to-consumer streaming platform](https://www.endeavorstreaming.com/platform/)


### eHealth Africa

**Software Engineer**

Kano, Nigeria, November 2019 - May 2024

Built and maintained production healthcare software across mobile, web, backend, and cross-platform environments, contributing to patient-facing products, healthcare operations, and digital commerce workflows connected to EHA Clinics.

- Developed and maintained cross-platform mobile features for Android and iOS using React Native, plus additional mobile work across Flutter and native Android.
- Implemented healthcare workflows covering appointments, patient information, medical records, laboratory services, medication and pharmaceutical ordering, payments, telemedicine, and patient communication.
- Built responsive web interfaces using React, JavaScript, and TypeScript for patient-facing and internal healthcare workflows.
- Developed Node.js and Express backend services, including REST APIs, server-side business logic, data access, and application integrations.
- Optimized application and database interactions to improve reliability, response times, and production behavior.
- Products: [Health-Mate](https://play.google.com/store/apps/details?id=ng.eha.healthmate&hl=en_GB), [EHA Clinics](https://www.eha.care/), [EHA Informatics](https://erp.eha.ng/services/informatics), and [GetCare](https://getcare.eha.ng/)


### Teal Technology Service (IBM OCP JV)

**Android Developer**

Abuja, Nigeria, April 2019 - April 2020

Developed and maintained Udongo, an offline-first Android application designed to support agricultural extension agents operating in environments with limited or unreliable internet connectivity.

- Designed and developed native Android features using the Android SDK, with a strong focus on reliability, usability, and performance on constrained mobile devices.
- Built and maintained offline-first data workflows, enabling agricultural extension agents to capture, access, and manage information without an active internet connection.
- Implemented local data persistence and background synchronization workflows to synchronize locally captured data with backend services when connectivity became available.
- Designed application flows to handle intermittent connectivity, synchronization failures, retries, and data consistency without disrupting field operations.
- Integrated application components with backend APIs and supported the end-to-end flow of data between mobile devices and remote services.
- Application: `ng.udongo.android`


### Biosec Solutions

**Software Engineer**

Abuja, Nigeria, April 2018 - May 2019

Built and maintained full-stack business applications spanning frontend, backend, mobile, and persistence layers, with a strong focus on secure, reliable, and offline-capable solutions for real-world business environments.

- Designed and developed backend services and REST APIs using Spring Boot, implementing business logic, data access, integrations, authentication, and application workflows.
- Developed native Android applications using the Android SDK and Kotlin/Java, delivering business-critical mobile applications for field and operational use.
- Built offline-first applications capable of operating reliably in environments with limited or intermittent connectivity, including local data persistence, synchronization, and recovery workflows.
- Integrated biometric and fingerprint hardware/software SDKs, including Neurotechnology fingerprint and biometric SDKs, to support biometric enrollment, identification, verification, and device integration.
- Participated throughout the software development lifecycle, including requirements analysis, technical design, architecture discussions, implementation, integration, testing, debugging, deployment, and release.
- Company: [Biosec Solutions](https://biosec.com.ng/)


## What I Build

<div class="capability-grid">
  <article>
    <h3>Cross-platform product surfaces</h3>
    <p>React Native, React, Flutter, Kotlin Multiplatform, and native Android interfaces for mobile, web, and TV contexts, with attention to input model, screen size, and release reliability.</p>
  </article>

  <article>
    <h3>Backend-connected applications</h3>
    <p>Node.js, Express, Spring Boot, REST API integration, data access flows, transactional workflows, and client/server debugging across production web and mobile products.</p>
  </article>

  <article>
    <h3>Offline-first mobile workflows</h3>
    <p>Android applications designed to keep core field operations available during poor connectivity, then synchronize cleanly when networks return.</p>
  </article>

  <article>
    <h3>Engineering delivery</h3>
    <p>Code review, performance diagnosis, regression testing, implementation planning, production support, technical mentoring, and AI-assisted development workflows.</p>
  </article>
</div>

## Profile

I am a senior software engineer with 7+ years of experience building production web, mobile, backend, and connected-TV applications, with expertise across Kotlin, Java, React Native, React, Flutter, TypeScript, Node.js, and Spring Boot. I have worked across streaming, healthcare, e-commerce, offline-first systems, and biometric integrations.

I work primarily with Kotlin, Kotlin Multiplatform, Java, JavaScript, TypeScript, React, React Native, Flutter, Node.js, Express, Spring Boot, REST APIs, and database-backed systems. I care about maintainable implementation, performance, reviewable architecture, testing, and practical delivery across real product constraints.

I also use AI-assisted engineering workflows for code exploration, refactoring, debugging, test generation, documentation, and technical research while keeping human review and production-quality judgment in the loop.

<dl class="profile-facts">
  <div>
    <dt>Location</dt>
    <dd>Abuja, Nigeria</dd>
  </div>
  <div>
    <dt>Primary domains</dt>
    <dd>Streaming, healthcare, mobile, backend services, connected TV</dd>
  </div>
  <div>
    <dt>Core stack</dt>
    <dd>React Native, React, Android, Kotlin, Kotlin Multiplatform, Java, TypeScript, Node.js, Express, Spring Boot</dd>
  </div>
</dl>


## Technical focus {#technical-focus}

**Languages:** Kotlin, Java, JavaScript, TypeScript, Python, HTML, CSS  
**Mobile:** React Native, native Android, Kotlin Multiplatform, Flutter  
**Web and backend:** React, Node.js, Express, Spring Boot, REST APIs, database-backed services  
**Engineering:** full-stack development, cross-platform development, offline-first architecture, responsive design, performance optimization, testing, debugging, code review, API integration, technical mentoring, AI-assisted development

## How I Work

I am strongest in product environments where the engineering work spans more than one layer of the stack. I can move from a mobile defect to the API behavior behind it, from a performance issue on a low-end Android device to the data shape causing it, or from a TV navigation requirement to a reusable cross-platform component.

My default working style is practical and reviewable: clarify the user flow, understand the failure mode or product requirement, make the smallest coherent implementation, test the affected path, and leave the code easier to reason about than I found it.

I use LLM coding tools as part of my engineering workflow for codebase exploration, alternate implementation research, test-case drafting, refactoring support, and documentation. I treat AI output as draft material that still needs engineering review, system context, and production judgment.

## Education

**B.Sc. Computer Science**  
Madonna University, Rivers, Nigeria

## Contact {#contact}

For engineering roles, product work, consulting, or technical collaboration:

- Email: [caleb.grimah@gmail.com](mailto:caleb.grimah@gmail.com)
- Alternate email: [caleb.grimah@arcadereality.org](mailto:caleb.grimah@arcadereality.org)
- GitHub: [@calebgrimah](https://github.com/calebgrimah)
- LinkedIn: [Caleb Grimah](https://www.linkedin.com/in/caleb-grimah-8678aa122/)
- Resume: [Download PDF]({{ '/assets/docs/caleb-grimah-resume.pdf' | relative_url }})
