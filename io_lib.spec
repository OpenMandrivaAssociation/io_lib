%define name	io_lib
%define version 1.12.2
%define release %mkrel 1
%define major	1
%define libname	%mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Name:		%{name}
Version:	1.13.0
Release:	1
Summary:	General purpose trace file library
License:	GPL
Group:		Development/C
Url:		http://staden.sourceforge.net/
Source0:		https://sourceforge.net/projects/staden/files/io_lib/1.13.0/%{name}-%{version}.tar.gz
BuildRequires:  zlib-devel

%description
Io_lib is a library of file reading and writing code to provide a general
purpose trace file (and Experiment File) reading interface. The programmer
simply calls the (eg) read_reading to create a "Read" C structure with the
data loaded into memory.

%package -n %{libname}
Summary:        Main library for %{name}
Group:          System/Libraries
Provides:       lib%{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run %{name}.

%package -n %{develname}
Summary:    Development header files for %{name}
Group:      Development/C
Requires:   %{libname} = %{version}-%{release}
Provides:   %{name}-devel = %{version}-%{release}
Obsoletes:  %mklibname -d %{name} 1.9.0

%description -n %{develname}
Libraries, include files and other resources you can use to develop
%{name} applications.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%files
%defattr (-,root,root)
%doc CHANGES COPYRIGHT README
%{_bindir}/*

%files -n %{libname}
%defattr (-,root,root)
%{_libdir}/libstaden-read.so.*

%files -n %{develname}
%defattr (-,root,root)
%{_includedir}/%{name}
%{_libdir}/libstaden-read.a
%{_libdir}/libstaden-read.so
%{_mandir}/*/*



%changelog
* Sat Feb 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.12.2-1mdv2011.0
+ Revision: 636154
- new version
- drop libtool patch, merged upstream

* Wed Dec 01 2010 Funda Wang <fwang@mandriva.org> 1.11.2.1-3mdv2011.0
+ Revision: 604352
- rebuild for new zlib

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.11.2.1-2mdv2010.0
+ Revision: 429515
- rebuild

* Mon Aug 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.11.2.1-1mdv2009.0
+ Revision: 270945
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Feb 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.10.2-1mdv2008.1
+ Revision: 162500
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.9.0-4mdv2008.1
+ Revision: 132445
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix autoconf-2.5x path
    - import io_lib


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.9.0-3mdv2007.0
- Rebuild

* Fri Jul 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.9.0-2mdk
- Fix BuildRequires

* Thu Jul 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.9.0-1mdk 
- new version
- spec cleanup 
- drop previous patch, no use anymore
- less strict requires between packages

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.8.12b-1mdk 
- new version
- new URL
- rpmbuildupdate aware

* Thu Jan 08 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.8.11-3mdk
- try to solve include problem

* Wed Jan 07 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.8.11-2mdk
- add missing include file

* Wed Dec 31 2003 Guillaume Rousse <guillomovitch@mandrake.org> 1.8.11-1mdk
- first mdk release

