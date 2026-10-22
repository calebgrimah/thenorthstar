source "https://rubygems.org"

# Local theme assets keep builds independent of remote theme downloads.
gem "jekyll", "~> 3.10"
gem "liquid", "~> 4.0", ">= 4.0.4"
gem "base64"
gem "bigdecimal"
gem "csv"
gem "ffi", "< 1.17"
gem "webrick"
gem "kramdown-parser-gfm"

group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.17"
  gem "jekyll-redirect-from", "~> 0.16"
  gem "jekyll-seo-tag", "~> 2.8"
end

platforms :windows, :jruby do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end

gem "wdm", "~> 0.1.1", platforms: :windows
