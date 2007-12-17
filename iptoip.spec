%define	name	iptoip
%define	version	0.3.0
%define	release	 %mkrel 0.5

%define	cvsver	20020115

Name:		%{name}
Summary:	Maintains a coherent ipvsadm table 
Version:	%{version}
Release:	%{release}
Source: 	%{name}-%{cvsver}.tar.bz2
Group:		Networking/Other
License:	GPL
Url:		http://iptoip.sourceforge.net
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

