Summary:	Netlab neural network software
Name:		netlab
Version:	3.2
Release:	0.1
License:	BSD
Group:		Applications/Math
Source0:	http://www.ncrg.aston.ac.uk/%{name}/%{name}.tar.gz
# Source0-md5:	c9b2ca3cd331dba1eadc648da8db8b35
Source1:	http://www.ncrg.aston.ac.uk/%{name}/nethelp.tar.gz
# Source1-md5:	750f81eaf3c9eb4d619494197d5cefea
URL:		http://www.ncrg.aston.ac.uk/netlab/
Requires:	octave
BuildRequires:	octave
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Netlab toolbox is designed to provide the central tools necessary
for the simulation of theoretically well founded neural network
algorithms and related models for use in teaching, research and
applications development.

Netlab has beed designed to be used with (commercial) Matlab software,
but it works well with Matlab-compatible GNU Octave.

%package doc
Summary:	Help files for Netlab neural network software
Group:		Applications/Math
Requires:	%{name}

%description doc
The Netlab toolbox help files.

%prep
%setup -q -a 0 -c %{name}
%setup -q -a 1 -c %{name}-doc

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT`octave-config --m-site-dir`/netlab/
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/
cp -a *.m $RPM_BUILD_ROOT`octave-config --m-site-dir`/netlab/
cp -a *.htm LICENSE $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}


%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f "%{_datadir}/octave/site/m/startup/octaverc" ] && \
	! grep -q "netlab" "%{_datadir}/octave/site/m/startup/octaverc"
then
	echo "LOADPATH = [ '$( octave-config --m-site-dir)/netlab/:', LOADPATH ];" >> "%{_datadir}/octave/site/m/startup/octaverc"
fi

%postun
if [ "$1" = "0" ]; then
	umask 027
	grep -E -v "netlab" "%{_datadir}/octave/site/m/startup/octaverc" > "%{_datadir}/octave/site/m/startup/octaverc.tmp"
	mv -f "%{_datadir}/octave/site/m/startup/octaverc.tmp" "%{_datadir}/octave/site/m/startup/octaverc"
fi

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}/LICENSE
%( octave-config --m-site-dir )/%{name}

%files doc
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}/*.htm
