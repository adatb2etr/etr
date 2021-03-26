select * from HELLOTEST;
TRUNCATE TABLE etradmin;
select * from etradmin;
select * from oktato;
select * from hallgato;
select * from elofeltetel;

CREATE TABLE etradmin(
    azonosito VARCHAR2(32) not null,
    vezeteknev VARCHAR2(64) not null,
    keresztnev VARCHAR2(64) not null,
    telefonszam VARCHAR2(64) not null,
    email VARCHAR2(64) not null,
    jelszo VARCHAR2(64) not null,
    CONSTRAINT azonositoAdmin_pk PRIMARY KEY (azonosito)
)

CREATE TABLE hallgato(
    azonosito VARCHAR2(6) not null,
    vezeteknev VARCHAR2(64) not null,
    keresztnev VARCHAR2(64) not null,
    szemelyiszam VARCHAR2(64) not null,
    telefonszam VARCHAR2(64) not null,
    email VARCHAR2(64) not null,
    jelszo VARCHAR2(64) not null,
    szulido DATE not null,
    teljesitettkreditek INT default 0,
    kepzes VARCHAR(64) not null,
    CONSTRAINT azonosito_pk PRIMARY KEY (azonosito)
);


CREATE TABLE oktato(
    azonosito VARCHAR2(6) not null,
    vezeteknev VARCHAR2(64) not null,
    keresztnev VARCHAR2(64) not null,
    szemelyiszam VARCHAR2(64) not null,
    telefonszam VARCHAR2(64) not null,
    email VARCHAR2(64) not null,
    jelszo VARCHAR2(64) not null,
    szulido DATE not null,
    CONSTRAINT oktatoazonosito_pk PRIMARY KEY (azonosito)
);


CREATE TABLE tartozasok(
    hallgatoAzonosito VARCHAR2(6),
    tartozasosszeg INT default 0,
    CONSTRAINT hallgatoTartozas_fk FOREIGN KEY (hallgatoAzonosito) REFERENCES hallgato(azonosito)
);

CREATE TABLE osztondij(
    hallgatoAzonosito VARCHAR2(6),
    osztondijosszeg INT default 0,
    CONSTRAINT hallgatoOsztondijfk FOREIGN KEY (hallgatoAzonosito) REFERENCES hallgato(azonosito)
);


CREATE TABLE terem(
    cim VARCHAR2(64) not null,
    kapacitas INT default 999 not null,
    CONSTRAINT teremHely_pk PRIMARY KEY (cim)
);

CREATE TABLE kurzus(
    kurzuskod VARCHAR2(20) not null,
    kurzusnev VARCHAR2(64) not null,
    ferohely INT default 999 not null,
    kredit INT default 1 not null,
    teremCim VARCHAR(64),
    oktatoAzonosito references oktato(azonosito),
    CONSTRAINT kurzuskod_pk PRIMARY KEY (kurzuskod),
    CONSTRAINT teremHely_fk FOREIGN KEY (teremCim) REFERENCES terem(cim)
);




CREATE TABLE elofeltetel(
    id NUMBER GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
    kurzusKod VARCHAR2(20) not null,
    elofeltetelKod VARCHAR2(20) not null,
    CONSTRAINT elofeltetelKurzuskod_fk FOREIGN KEY (kurzusKod) REFERENCES kurzus(kurzuskod),
    CONSTRAINT elofeltetelKurzuskod_fk2 FOREIGN KEY (elofeltetelKod) REFERENCES kurzus(kurzuskod)
);

CREATE TABLE idopont(
    id NUMBER GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
    kezdete timestamp not null,
    vege timestamp not null,
    kurzusKod VARCHAR(20) not null,
    CONSTRAINT kezdesVege_pk PRIMARY KEY (kezdete, vege),
    CONSTRAINT idopontKurzusKod_fk FOREIGN KEY (kurzusKod) REFERENCES kurzus(kurzuskod)
);

CREATE TABLE vizsga(
    vizsgaID NUMBER GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
    kurzusKod VARCHAR2(20) not null,
    idopont timestamp not null,
    ferohely INT DEFAULT 999 NOT NULL,
    CONSTRAINT vizsgaID_pk PRIMARY KEY (vizsgaID),
    CONSTRAINT vizsgaKurzusKod_fk FOREIGN KEY (kurzusKod) REFERENCES kurzus(kurzuskod)
);

select * from vizsga;
drop table vizsga;

CREATE TABLE vizsgazik(
    id NUMBER GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
    vizsgaID NUMBER not null,
    hallgatoAzonosito VARCHAR(6) not null,
    kapottjegy INT not null check (kapottjegy between 1 and 5),
    vizsgaalkalom INT default 0 not null check (vizsgaalkalom between 0 and 3),
    CONSTRAINT vizsgaID_fk FOREIGN KEY (vizsgaID) REFERENCES vizsga(vizsgaID),
    CONSTRAINT vizsgaHallgatoAzonostio_pk FOREIGN KEY (hallgatoAzonosito) REFERENCES hallgato(azonosito)
);

drop table vizsgazik;

CREATE TABLE kurzustfelvesz(
    id NUMBER GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
    hallgatoAzonosito VARCHAR2(6) not null,
    kurzusKod VARCHAR2(20) not null,
    teljesitette NUMBER(1) DEFAULT 0,
    CONSTRAINT kurzusHallgatoAzonosito_fk FOREIGN KEY (hallgatoAzonosito) REFERENCES hallgato(azonosito),
    CONSTRAINT kurzusKurzusKod_fk FOREIGN KEY (kurzusKod) REFERENCES kurzus(kurzuskod)
);

select * from kurzus;
select * from hallgato;
drop table kurzustfelvesz;
drop table vizsgazik;
drop table vizsga;
drop table idopont;
drop table elofeltetel;
drop table kurzus;
drop table terem;
drop table osztondij;
drop table tartozasok;
drop table kezeloktatot;
drop table kezelhallgatot;
drop table hallgato;
drop table oktato;
drop table etradmin;

