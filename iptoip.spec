%define	name	iptoip
%define	version	0.3.0
%define release	 0.8

%define	cvsver	20020115

Name:		%{name}
Summary:	Maintains a coherent ipvsadm table 
Version:	%{version}
Release:	%{release}
Source: 	%{name}-%{cvsver}.tar.bz2
Group:		Networking/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
License:	GPL
Url:		https://iptoip.sourceforge.net
Requires:	perl perl-XML-Simple >= 1.05
Requires:	perl-XML-Parser , ipvsadm
Requires(post,preun):	rpm-helper
Buildarch:	noarch


%description
iptoip is a program to maintain an ipvsadm table coherent.
It is specially useful when using an intermittent internet
connection or when your ISP breaks conections to reaffect IP 
addresses (like in France). Use the ipvsadm tool to build
and update a forwarding table. 


%prep
%setup -q -n %name

%build

%install
rm -rf $RPM_BUILD_ROOT

install -m 755 %{name} -D $RPM_BUILD_ROOT%_sbindir/%{name}
install -m 755 %{name}.init -D $RPM_BUILD_ROOT%_initrddir/%{name}
install -m 644 %{name}.xml -D $RPM_BUILD_ROOT%_sysconfdir/%{name}.xml
install -m 644 %{name}.8 -D $RPM_BUILD_ROOT%_mandir/man8/%{name}.8
install -m 644 %{name}.xml.5 -D $RPM_BUILD_ROOT%_mandir/man5/%{name}.xml.5


%clean
rm -rf $RPM_BUILD_ROOT 

%post
%_post_service %{name}


%preun
%_preun_service %{name}


%files
%defattr(-,root,root,0755)
%doc README CHANGELOG AUTHORS COPYING TODO
%config(noreplace) %_initrddir/*
%_sbindir/*
%_mandir/man5/*
%_mandir/man8/*
%config(noreplace) %_sysconfdir/%{name}.xml



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-0.7mdv2011.0
+ Revision: 619680
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.3.0-0.6mdv2010.0
+ Revision: 429524
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.3.0-0.5mdv2009.0
+ Revision: 140792
- restore BuildRoot

* Tue Dec 18 2007 Thierry Vignaud <tv@mandriva.org> 0.3.0-0.5mdv2008.1
+ Revision: 131784
- fix prereq on rpm-helper
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import iptoip


* Thu Aug 19 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.3.0-0.5mdk
- rebuild

* Tue Jul 22 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.3.0-0.4mdk
- rebuild
- rm -rf $RPM_BUILD_ROOT in %%install, not %%prep
- cosmetics
- macroize

* Mon Dec 16 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.3.0-0.3mdk
- noarch

* Tue Jan 15 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.3.0-0.2mdk
- cvs 20020115 ( fix & enhance syslog output )

* Wed Dec 12 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.3.0-0.1mdk
- 0.3.0

* Sun Nov 11 2001  Lenny Cartier <lenny@mandrakesoft.com> 0.2.0-1mdk
- upgraded to stable 0.2.0

* Wed Nov 07 2001 Philippe Libat <philippe@mandrakesoft.com> 0.1.7-2mdk
- add perl-XML-Parser,ipvsadm require

* Sun Sep 09 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.1.7-1mdk
- 0.1.7

* Wed Jul 04 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.1.6-1mdk
- updated to 0.1.6

* Mon Apr 16 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.1.4-1mdk
- updated to 0.1.4

* Tue Apr 10 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.1.3-1mdk
- updated to 0.1.3

* Wed Apr 04 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.1.2-1mdk
- updated to 0.1.2
- added initscript from Philippe Libat at Mandrakesoft.

* Wed Mar 07 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.1.1-1mdk
- new in contribs

