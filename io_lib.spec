%define name	io_lib
%define version 1.10.2
%define release %mkrel 3
%define major	%{version}
%define libname	%mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	General purpose trace file library
License:	GPL
Group:		Development/C
Url:		http://staden.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/staden/%{name}-%{version}.tar.gz
Patch:      io_lib-1.10.2-libtool.patch
BuildRequires:  zlib1-devel
Buildroot:	%{_tmppath}/%{name}-%{version}

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
%patch -p1

%build
autoreconf -i
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr (-,root,root)
%doc CHANGES COPYRIGHT README
%{_bindir}/*

%files -n %{libname}
%defattr (-,root,root)
%{_libdir}/libread-%{major}.so

%files -n %{develname}
%defattr (-,root,root)
%{_includedir}/%{name}
%{_libdir}/libread.a
%{_libdir}/libread.la
%{_libdir}/libread.so
%{_mandir}/*/*

