%define _optdir	/opt

Name:       media-data
Summary:    Media data. Image/Sounds/Videos and Others.
Version:    0.1.66
Release:    1
Group:      TO_BE/FILLED_IN
License:    TO_BE/FILLED_IN
Source0:    %{name}-%{version}.tar.gz
BuildRequires: cmake


%description
Description: Media data. Image/Sounds/Videos and Others.


%prep
%setup -q
LDFLAGS+="-Wl,--rpath=%{PREFIX}/lib -Wl,--as-needed -Wl,--hash-style=both"; export LDFLAGS

cmake . -DCMAKE_INSTALL_PREFIX=%{_optdir}

%build
make %{?jobs:-j%jobs}

%install
%make_install

%files
%defattr(-,root,root,-)
%{_optdir}/data/file-manager-service/.thumb/*
%{_optdir}/media/Downloads/Others/*
%{_optdir}/share/settings/Ringtones/*
%{_optdir}/share/settings/Wallpapers/*
%{_optdir}/share/settings/Alerts/*
"%{_optdir}/media/Images and videos/My photo clips/1_photo.jpg"
"%{_optdir}/media/Images and videos/My photo clips/2_photo.jpg"
"%{_optdir}/media/Images and videos/My photo clips/3_photo.jpg"
"%{_optdir}/media/Images and videos/My photo clips/4_photo.jpg"
"%{_optdir}/media/Images and videos/My photo clips/5_photo.JPG"
"%{_optdir}/media/Images and videos/My video clips/Helicopter.mp4"
"%{_optdir}/media/Images and videos/Wallpapers/Default.png"
"%{_optdir}/media/Images and videos/Wallpapers/Home_default.png"
"%{_optdir}/media/Sounds and music/Music/Over the horizon.mp3"

