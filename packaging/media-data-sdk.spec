#sbs-git:slp/pkgs/m/media-data media-data 0.1.91 bf79c07d3fb5086d1bf9a99771a956c804a5a736
%define _optdir	/opt

Name:       media-data-sdk
Summary:    Media data for SDK. Image/Sounds/Videos and Others.
Version: 0.1.13
Release:    1
Group:      Service  
License:    Apache-2.0  
Source0:    %{name}-%{version}.tar.gz
Source1001: packaging/media-data-sdk.manifest 
BuildRequires: cmake


%description
Description: Media data for SDK. Image/Sounds/Videos and Others.


%prep
%setup -q
LDFLAGS+="-Wl,--rpath=%{PREFIX}/lib -Wl,--as-needed -Wl,--hash-style=both"; export LDFLAGS

cmake . -DCMAKE_INSTALL_PREFIX=%{_optdir}

%build
cp %{SOURCE1001} .
make %{?jobs:-j%jobs}

%install
%make_install


%post
if [ ! -d /opt/dbspace ]; then  
    mkdir -p /opt/dbspace  
fi

rm -rf /opt/dbspace/.media.db*
sqlite3 /opt/dbspace/.media.db 'PRAGMA journal_mode = PERSIST;
	CREATE TABLE visual_folder(folder_uuid VARCHAR(256) PRIMARY KEY, path VARCHAR(256), folder_name VARCHAR(256), modified_date INT, web_account_id VARCHAR(256), storage_type INT, sns_type INT, lock_status INT, web_album_id VARCHAR(256), valid INT, unique(path, folder_name, web_album_id, storage_type) );
	INSERT INTO "visual_folder" VALUES("31e8854f-fa38-499c-ad0b-ebd7fc195f72","/opt/media/Images","Images",946990496,"",0,0,0,"",1);
	INSERT INTO "visual_folder" VALUES("e81fcc9c-ce4c-478c-b8de-6f3abc4219ae","/opt/media/Images/Wallpapers","Wallpapers",946990496,"",0,0,0,"",1);
	CREATE TABLE image_meta(_id INTEGER PRIMARY KEY AUTOINCREMENT, visual_uuid VARCHAR(256), longitude DOUBLE, latitude DOUBLE, description VARCHAR(256), width INT, height INT, orientation INT, datetaken INT, unique(visual_uuid) );
	INSERT INTO "image_meta" VALUES(1,"d523de83-1bd3-4420-b3ae-30cc09fadd7e",1000.0,1000.0,"No description",0,0,1,1328593573);
	INSERT INTO "image_meta" VALUES(2,"bce4c371-3567-4393-80c9-03696e95cf72",1000.0,1000.0,"No description",0,0,1,1328594459);
	INSERT INTO "image_meta" VALUES(3,"acc3f51a-06ed-4eeb-9589-4ec8471aebc0",1000.0,1000.0,"No description",1280,720,1,1328680445);
	INSERT INTO "image_meta" VALUES(4,"859f496f-9c93-402a-8fa9-bbadccca017d",1000.0,1000.0,"No description",1280,720,1,1328593816);
	INSERT INTO "image_meta" VALUES(5,"a911ce7d-30e9-45fe-8f01-ca0fecb359c9",1000.0,1000.0,"No description",720,1280,1,1319103726);
	INSERT INTO "image_meta" VALUES(6,"257849e1-03d0-401a-bfeb-88374fed528a",1000.0,1000.0,"No description",1280,720,1,1319103804);
	INSERT INTO "image_meta" VALUES(7,"64c33db5-74dd-46c9-b31c-945278127cf8",1000.0,1000.0,"No description",0,0,1,1319103711);
	INSERT INTO "image_meta" VALUES(8,"fb07a723-63a7-4591-bcf6-950de63f9dd6",1000.0,1000.0,"No description",0,0,1,1328594351);
	INSERT INTO "image_meta" VALUES(9,"91b21d6e-a642-4b0f-a221-b30048ca907c",1000.0,1000.0,"                               ",1280,720,1,1328593485);
	INSERT INTO "image_meta" VALUES(10,"f402c7be-4121-49d9-97a1-3be23314d6e5",1000.0,1000.0,"No description",0,0,1,1319103566);
	INSERT INTO "image_meta" VALUES(11,"d678a3c3-2594-4743-b7ec-204094877005",1000.0,1000.0,"No description",0,0,1,1328684387);
	INSERT INTO "image_meta" VALUES(12,"edfe77a5-da1b-4cb3-83fb-90fea7dce551",1000.0,1000.0,"No description",0,0,1,1328594384);
	INSERT INTO "image_meta" VALUES(13,"32711540-7b16-40c1-8d71-80092f94ccea",1000.0,1000.0,"No description",1280,720,1,1328593514);
	INSERT INTO "image_meta" VALUES(14,"b64c439e-8cd2-4901-8d0e-b69a192cfd9e",1000.0,1000.0,"No description",720,1280,1,1328593777);
	INSERT INTO "image_meta" VALUES(15,"b3efff75-34be-456d-97bb-bb5e1307751f",1000.0,1000.0,"No description",0,0,1,1319158904);
	INSERT INTO "image_meta" VALUES(16,"a442ad71-3f55-4d57-8ec1-63745bb43de8",1000.0,1000.0,"No description",1280,720,1,1319103819);
	INSERT INTO "image_meta" VALUES(17,"60f9d85a-324d-414b-804c-b8e627ddb4ba",1000.0,1000.0,"No description",720,1280,1,1328593473);
	INSERT INTO "image_meta" VALUES(18,"8baca8e4-cb80-49c3-b994-6597b67b7a89",1000.0,1000.0,"No description",0,0,1,1319103686);
	CREATE TABLE visual_media(visual_uuid VARCHAR(256) PRIMARY KEY, path VARCHAR(256), folder_uuid VARCHAR(256), display_name VARCHAR(256), content_type INT, rating INT, modified_date INT, thumbnail_path VARCHAR(256), http_url VARCHAR(256), size INT, valid INT, unique(path, folder_uuid, display_name) );
	INSERT INTO "visual_media" VALUES("d523de83-1bd3-4420-b3ae-30cc09fadd7e","/opt/media/Images/image3.jpg","31e8854f-fa38-499c-ad0b-ebd7fc195f72","image3.jpg",1,0,1328593576,"/opt/data/file-manager-service/.thumb/phone/.jpg-03bdfd7e4d43c736819639b84a590b5f.jpg","",0,1);
	INSERT INTO "visual_media" VALUES("bce4c371-3567-4393-80c9-03696e95cf72","/opt/media/Images/image15.jpg","31e8854f-fa38-499c-ad0b-ebd7fc195f72","image15.jpg",1,0,1328594460,"/opt/data/file-manager-service/.thumb/phone/.jpg-de79768105a730492b3b28ca33ff89f4.jpg","",0,1);
	INSERT INTO "visual_media" VALUES("acc3f51a-06ed-4eeb-9589-4ec8471aebc0","/opt/media/Images/image2.jpg","31e8854f-fa38-499c-ad0b-ebd7fc195f72","image2.jpg",1,0,1328680448,"/opt/data/file-manager-service/.thumb/phone/.jpg-93d14e2e94dfbccc9f38a14c4be6a780.jpg","",0,1);
	INSERT INTO "visual_media" VALUES("859f496f-9c93-402a-8fa9-bbadccca017d","/opt/media/Images/image12.jpg","31e8854f-fa38-499c-ad0b-ebd7fc195f72","image12.jpg",1,0,1328593818,"/opt/data/file-manager-service/.thumb/phone/.jpg-e32fd6fd44abe296c14de2407bab1f93.jpg","",0,1);
	INSERT INTO "visual_media" VALUES("a911ce7d-30e9-45fe-8f01-ca0fecb359c9","/opt/media/Images/image16.jpg","31e8854f-fa38-499c-ad0b-ebd7fc195f72","image16.jpg",1,0,1319103728,"/opt/data/file-manager-service/.thumb/phone/.jpg-aa5afe63b8aaa41079f9f37297d0763f.jpg","",0,1);
	INSERT INTO "visual_media" VALUES("257849e1-03d0-401a-bfeb-88374fed528a","/opt/media/Images/image10.jpg","31e8854f-fa38-499c-ad0b-ebd7fc195f72","image10.jpg",1,0,1319103806,"/opt/data/file-manager-service/.thumb/phone/.jpg-70a952ceff9175115b8c3fd044cdf978.jpg","",0,1);
	INSERT INTO "visual_media" VALUES("64c33db5-74dd-46c9-b31c-945278127cf8","/opt/media/Images/image7.jpg","31e8854f-fa38-499c-ad0b-ebd7fc195f72","image7.jpg",1,0,1319103714,"/opt/data/file-manager-service/.thumb/phone/.jpg-fc4557b53139ca8f35a3f13cea24ed13.jpg","",0,1);
	INSERT INTO "visual_media" VALUES("fb07a723-63a7-4591-bcf6-950de63f9dd6","/opt/media/Images/image13.jpg","31e8854f-fa38-499c-ad0b-ebd7fc195f72","image13.jpg",1,0,1328594354,"/opt/data/file-manager-service/.thumb/phone/.jpg-825ded447a3ce04d14d737f93d7cee26.jpg","",0,1);
	INSERT INTO "visual_media" VALUES("91b21d6e-a642-4b0f-a221-b30048ca907c","/opt/media/Images/image4.jpg","31e8854f-fa38-499c-ad0b-ebd7fc195f72","image4.jpg",1,0,1328593488,"/opt/data/file-manager-service/.thumb/phone/.jpg-8ea059905f24eea065a7998dc5ff1f7e.jpg","",0,1);
	INSERT INTO "visual_media" VALUES("f402c7be-4121-49d9-97a1-3be23314d6e5","/opt/media/Images/image6.jpg","31e8854f-fa38-499c-ad0b-ebd7fc195f72","image6.jpg",1,0,1319103570,"/opt/data/file-manager-service/.thumb/phone/.jpg-10555c13cdfe5a763a69e08489de3c70.jpg","",0,1);
	INSERT INTO "visual_media" VALUES("d678a3c3-2594-4743-b7ec-204094877005","/opt/media/Images/image1.jpg","31e8854f-fa38-499c-ad0b-ebd7fc195f72","image1.jpg",1,0,1328684390,"/opt/data/file-manager-service/.thumb/phone/.jpg-f5052c8428c4a22231d6ece0c63b74bd.jpg","",0,1);
	INSERT INTO "visual_media" VALUES("edfe77a5-da1b-4cb3-83fb-90fea7dce551","/opt/media/Images/image14.jpg","31e8854f-fa38-499c-ad0b-ebd7fc195f72","image14.jpg",1,0,1328594386,"/opt/data/file-manager-service/.thumb/phone/.jpg-6f7e6adae30603c45be7db083610d0a3.jpg","",0,1);
	INSERT INTO "visual_media" VALUES("32711540-7b16-40c1-8d71-80092f94ccea","/opt/media/Images/image5.jpg","31e8854f-fa38-499c-ad0b-ebd7fc195f72","image5.jpg",1,0,1328593516,"/opt/data/file-manager-service/.thumb/phone/.jpg-c468b6d8820bfc0d9311d76f6575251a.jpg","",0,1);
	INSERT INTO "visual_media" VALUES("b64c439e-8cd2-4901-8d0e-b69a192cfd9e","/opt/media/Images/image11.jpg","31e8854f-fa38-499c-ad0b-ebd7fc195f72","image11.jpg",1,0,1328593780,"/opt/data/file-manager-service/.thumb/phone/.jpg-773fffb8f086e5954f15407b41c2635d.jpg","",0,1);
	INSERT INTO "visual_media" VALUES("b3efff75-34be-456d-97bb-bb5e1307751f","/opt/media/Images/image8.jpg","31e8854f-fa38-499c-ad0b-ebd7fc195f72","image8.jpg",1,0,1319158906,"/opt/data/file-manager-service/.thumb/phone/.jpg-5876701a15ec16bd0226ed00044cad92.jpg","",0,1);
	INSERT INTO "visual_media" VALUES("a442ad71-3f55-4d57-8ec1-63745bb43de8","/opt/media/Images/image9.jpg","31e8854f-fa38-499c-ad0b-ebd7fc195f72","image9.jpg",1,0,1319103822,"/opt/data/file-manager-service/.thumb/phone/.jpg-e82b0d23bfecbddaad1b98be7674b96e.jpg","",0,1);
	INSERT INTO "visual_media" VALUES("60f9d85a-324d-414b-804c-b8e627ddb4ba","/opt/media/Images/Wallpapers/Home_default.jpg","e81fcc9c-ce4c-478c-b8de-6f3abc4219ae","Home_default.jpg",1,0,1328593476,"/opt/data/file-manager-service/.thumb/phone/.jpg-66784c0b912f077f0a8de56a2f56161e.jpg","",0,1);
	INSERT INTO "visual_media" VALUES("8baca8e4-cb80-49c3-b994-6597b67b7a89","/opt/media/Images/Wallpapers/Default.jpg","e81fcc9c-ce4c-478c-b8de-6f3abc4219ae","Default.jpg",1,0,1319103690,"/opt/data/file-manager-service/.thumb/phone/.jpg-a19569ad296e9655d1fbf216f195f801.jpg","",0,1);
	CREATE TABLE video_bookmark(_id INTEGER PRIMARY KEY AUTOINCREMENT, visual_uuid VARCHAR(256), marked_time INT, thumbnail_path VARCHAR(256), unique( visual_uuid, marked_time) );
	CREATE TABLE video_meta(_id INTEGER PRIMARY KEY AUTOINCREMENT, visual_uuid VARCHAR(256), album VARCHAR(256), artist VARCHAR(256), title VARCHAR(256), genre VARCHAR(256), description VARCHAR(256), youtube_category VARCHAR(256), last_played_time INT, duration INT, longitude DOUBLE, latitude DOUBLE, width INT, height INT, datetaken INT, unique(visual_uuid) );
	CREATE TABLE web_streaming(_id INTEGER PRIMARY KEY AUTOINCREMENT, folder_id INT, folder_uuid VARCHAR(256), title VARCHAR(256), duration INT, url VARCHAR(256), thumb_path VARCHAR(256));
	CREATE TABLE visual_tag_map(_id INTEGER PRIMARY KEY AUTOINCREMENT, visual_uuid VARCHAR(256), tag_id INT, unique( visual_uuid, tag_id) );
	CREATE TABLE visual_tag(_id INTEGER PRIMARY KEY AUTOINCREMENT, tag_name VARCHAR(256), unique( tag_name) );
	CREATE TABLE audio_media (audio_uuid text primary key, path text unique, file_name text, thumbnail_path text, title text, album text, artist text, genre text, author text, year integer default -1, copyright text, description text, format text, bitrate integer default -1, track_num integer default -1, duration integer default -1, rating integer default 0, played_count integer default 0, last_played_time integer default -1, added_time integer, rated_time integer, album_rating integer default 0, modified_date integer default 0, size integer default 0, category INTEGER default 0, valid integer default 0, folder_uuid TEXT NOT NULL, storage_type integer, favourite   integer default 0, content_type integer default 3);
	CREATE TABLE audio_folder (folder_uuid TEXT primary key, path text, folder_name text, storage_type integer, modified_date integer default 0);
	CREATE TABLE audio_playlists (_id integer primary key autoincrement, name TEXT NOT NULL UNIQUE);
	CREATE TABLE audio_playlists_map (_id integer primary key autoincrement, playlist_id integer, audio_uuid TEXT NOT NULL, play_order INTEGER);
	DELETE FROM sqlite_sequence;
	INSERT INTO "sqlite_sequence" VALUES("image_meta",19);
	INSERT INTO "sqlite_sequence" VALUES("video_meta",1);
	CREATE INDEX f_mid_idx on visual_media(folder_uuid);
	CREATE INDEX fid_idx on visual_folder(folder_uuid);
	CREATE INDEX m_date_idx on visual_media(modified_date);
	CREATE INDEX mid_idx on visual_media(visual_uuid);
	CREATE VIEW item_view AS select visual_uuid as item_id, path as file_path, display_name,thumbnail_path as thumbnail,modified_date as date_modified, folder_uuid, rating as favourite, content_type from visual_media where valid=1 union select  audio_uuid ,path ,title ,thumbnail_path, modified_date, folder_uuid, favourite, content_type from audio_media;
	CREATE VIEW mediainfo_folder AS select folder_uuid, path, folder_name as name, storage_type from visual_folder where valid=1 union select folder_uuid, path, folder_name, storage_type from audio_folder;
'

chgrp 6017 /opt/dbspace/.media.db
chgrp 6017 /opt/dbspace/.media.db-journal

chmod 664 /opt/dbspace/.media.db
chmod 664 /opt/dbspace/.media.db-journal

chgrp 5000 /opt/data/file-manager-service/.thumb
chgrp 5000 /opt/data/file-manager-service/.thumb/phone
chgrp 5000 /opt/data/file-manager-service/.thumb/mmc

##resources
chown :5000 /opt/dbspace
chown :5000 /opt/data/file-manager-service/.thumb/phone/.[a-z0-9]*.*

##resources
chmod 775 /opt/data/file-manager-service/.thumb
chmod 775 /opt/data/file-manager-service/.thumb/phone
chmod 775 /opt/data/file-manager-service/.thumb/mmc
rm /opt/media/Downloads/.gitignore
rm /opt/media/Music/.gitignore
rm /opt/media/Videos/.gitignore
rm /opt/media/Camera\ shots/.gitignore
rm /opt/media/Music/Voice\ recorder/.gitignore
rm /opt/media/Music/FM\ Radio/.gitignore
rm /opt/media/Bookmark/.gitignore
rm /opt/media/RSS/.gitignore
rm /opt/media/Alerts\ and\ ringtones/Alerts/*.*
rm /opt/media/Alerts\ and\ ringtones/Ringtones/*.*

%files
%manifest media-data-sdk.manifest
%defattr(-,root,root,-)
%{_optdir}/data/file-manager-service/plugin-config
%{_optdir}/data/file-manager-service/.thumb/*
%{_optdir}/share/settings/*
%{_optdir}/media/*

