Summary:	Simulation program based on rigid body systems
Summary(pl):	Program do symulacji opartych na uk³adach bry³y sztywnej
Name:		aero
Version:	1.7.0
Release:	0.1
License:	Public Domain
Group:		Applications
Source0:	http://robotics.ee.uwa.edu.au/aero/ftp/%{name}_%{version}_src.tar.gz
# Source0-md5:	2ea6f065bc77162ce6b4f4c4a17a3636
URL:		http://robotics.ee.uwa.edu.au/aero/ftp/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AERO is a simulation program based on rigid body systems. With the
built-in 3D editor you can create a virtual scene consisting of
spheres, boxes (cuboids), cylinders and plains. These objects may be
connected with links like spring, damper, rod and joint.

%description -l pl
AERO to program do symulacji opartych na uk³adach bry³y sztywnej. Przy
u¿yciu wbudowanego edytora 3D mo¿na tworzyæ sceny wirtualne sk³adaj±ce
siê ze sfer, prostopad³o¶cianów, cylindrów i p³aszczyzn. Obiekty te
mo¿na ³±czyæ elementami takimi jak sprê¿yny, t³umiki, prêty i z³±cza.

%prep
%setup -q -n %{name}
cp src/Makefile{.linux,}

%build

cd src 
%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with ldconfig}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%endif

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

%if 0
# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%endif
