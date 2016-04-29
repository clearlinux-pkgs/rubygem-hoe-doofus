#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-hoe-doofus
Version  : 1.0.0
Release  : 11
URL      : https://rubygems.org/downloads/hoe-doofus-1.0.0.gem
Source0  : https://rubygems.org/downloads/hoe-doofus-1.0.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-hoe
BuildRequires : rubygem-minitest
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-test-unit

%description
= Hoe is a Doofus
* http://github.com/jbarnette/hoe-doofus
== Description
A Hoe plugin that helps me (and you, maybe?) keep from messing up gem
releases. It shows a configurable checklist when <tt>rake release</tt>
is run, and provides a chance to abort if anything's been forgotten.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n hoe-doofus-1.0.0
gem spec %{SOURCE0} -l --ruby > rubygem-hoe-doofus.gemspec

%build
gem build rubygem-hoe-doofus.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
hoe-doofus-1.0.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/hoe-doofus-1.0.0
rake --trace test TESTOPTS="-v"
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/hoe-doofus-1.0.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/hoe-doofus-1.0.0/.autotest
/usr/lib64/ruby/gems/2.3.0/gems/hoe-doofus-1.0.0/CHANGELOG.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/hoe-doofus-1.0.0/Manifest.txt
/usr/lib64/ruby/gems/2.3.0/gems/hoe-doofus-1.0.0/README.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/hoe-doofus-1.0.0/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/hoe-doofus-1.0.0/lib/hoe/doofus.rb
/usr/lib64/ruby/gems/2.3.0/specifications/hoe-doofus-1.0.0.gemspec
