# thenorthstar

A minimal Jekyll portfolio and journal. Theme styles, fonts, illustrations, and scripts are local; no remote theme download is needed.

## Run locally

Install Ruby, Bundler, and the native build tools for your operating system, then run:

```sh
bundle config set --local path vendor/bundle
bundle install
bundle exec jekyll serve --livereload
```

Open http://localhost:4000. Restart the server after changing `_config.yml` or `Gemfile`.

## Check the site

```sh
bundle exec jekyll build
python3 scripts/check_site.py
```

The checker verifies generated pages, local assets, links, anchor targets, heading counts, and duplicate IDs. For a subfolder deployment:

```sh
bundle exec jekyll build --baseurl /preview --destination /tmp/thenorthstar-preview
python3 scripts/check_site.py /tmp/thenorthstar-preview --baseurl /preview
```

## Content and design

- Edit shared Astera, Omari, and ArcadeReality summaries and project details in `_data/featured_projects.yml`.
- The homepage is `index.markdown`; the full portfolio is `calebgrimah.markdown`.
- Journal entries live in `_posts`; their `description` fields supply archive summaries.
- Keep the monospace type, narrow reading column, and restrained spacing. A faint dot texture sits behind the content. Native smooth anchor scrolling, brief click feedback, and one-time scroll entrances respect reduced-motion settings. Content stays visible without JavaScript.

## Deployment

Pull requests targeting `master` build and validate the site with Ruby 3.3. Merging into `master` runs the same build and publishes its checked output to `gh-pages`, the existing GitHub Pages source branch. `CNAME` preserves `thenorthstar.tech`. Pull requests do not publish to the live site.
