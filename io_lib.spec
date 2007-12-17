%define name	io_lib
%define version 1.9.0
%define release %mkrel 3
%define major	1.9.0
%define libname	%mklibname %{name} %{major}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	General purpose trace file library
License:	GPL
Group:		Development/C
Source:		http://prdownloads.sourceforge.net/staden/%{name}-%{version}.tar.bz2
Patch:		%{name}-1.9.0.autoconf.patch.bz2
Url:		http://staden.sourceforge.net/
BuildRequires:	automake1.9
BuildRequires:  zlib1-devel

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

%package -n %{libname}-devel
Summary:        Development header files for %{name}
Group:          Development/C
Requires:       %{libname} = %{version}
Provides:       lib%{name}-devel = %{version}-%{release}

%description -n %{libname}-devel
Libraries, include files and other resources you can use to develop
%{name} applications.

%prep
%setup -q
%patch -p 1

%build
libtoolize --force
aclocal-1.9
autoconf
automake-1.9
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall
chmod 644 %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr (-,root,root)
%doc CHANGES COPYRIGHT README
%{_bindir}/*

%files -n %{libname}
%defattr (-,root,root)
%{_libdir}/libread-%{major}.so

%files -n %{libname}-devel
%defattr (-,root,root)
%{_includedir}/%{name}
%{_libdir}/libread.a
%{_libdir}/libread.la
%{_libdir}/libread.so
%{_mandir}/*/*

