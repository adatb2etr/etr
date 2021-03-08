select * from HELLOTEST;
TRUNCATE TABLE etradmin;
select * from etradmin;
select * from oktato;
select * from hallgato;


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


CREATE TABLE kezelhallgatot(
    adminAzonosito VARCHAR2(32) not null,
    hallgatoAzonosito VARCHAR2(6) not null,
    folyamatleiras VARCHAR2(4000) not null,
    datum TIMESTAMP not null,
    CONSTRAINT adminAzonositoHallgato_pk FOREIGN KEY (adminAzonosito) REFERENCES etradmin(azonosito),
    CONSTRAINT hallgatoktatoAzonosito_pk FOREIGN KEY (hallgatoAzonosito) REFERENCES oktato(azonosito)
);

CREATE TABLE kezeloktatot(
    adminAzonosito VARCHAR2(32) not null,
    oktatoAzonosito VARCHAR2(6) not null,
    folyamatleiras VARCHAR2(4000) not null,
    datum TIMESTAMP not null,
    CONSTRAINT adminAzonositoOktato_pk FOREIGN KEY (adminAzonosito) REFERENCES etradmin(azonosito),
    CONSTRAINT kezeloktatoAzonosito_pk FOREIGN KEY (oktatoAzonosito) REFERENCES oktato(azonosito)
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
    kezdete timestamp not null,
    vege timestamp not null,
    ferohely INT default 999 not null,
    teremCim VARCHAR(64),
    oktatoAzonosito references oktato(azonosito),
    CONSTRAINT kurzuskod_pk PRIMARY KEY (kurzuskod),
    CONSTRAINT teremHely_fk FOREIGN KEY (teremCim) REFERENCES terem(cim)
);

CREATE TABLE idopont(
    kezdete timestamp not null,
    vege timestamp not null,
    kurzusKod VARCHAR(20) not null,
    CONSTRAINT kezdesVege_pk PRIMARY KEY (kezdete, vege),
    CONSTRAINT idopontKurzusKod_fk FOREIGN KEY (kurzusKod) REFERENCES kurzus(kurzuskod)
);

CREATE TABLE vizsga(
    kurzusKod VARCHAR2(20) not null,
    idopont timestamp not null,
    ferohely INT default 999 not null,
    CONSTRAINT vizsgaIdopont_pk PRIMARY KEY (idopont),
    CONSTRAINT vizsgaKurzusKod_fk FOREIGN KEY (kurzusKod) REFERENCES kurzus(kurzuskod)
);

CREATE TABLE vizsgazik(
    vizsgaKurzuskod VARCHAR(20) not null,
    vizsgaIdopont timestamp not null,
    hallgatoAzonosito VARCHAR(6) not null,
    kapottjegy INT not null check (kapottjegy between 1 and 5),
    vizsgaalkalom INT default 0 not null check (vizsgaalkalom between 0 and 3),
    CONSTRAINT vizsgaIdopont_fk FOREIGN KEY (vizsgaIdopont) REFERENCES vizsga(idopont),
    CONSTRAINT vizsgazikKurzuskod_fk FOREIGN KEY (vizsgaKurzuskod) REFERENCES kurzus(kurzuskod),
    CONSTRAINT vizsgaHallgatoAzonostio_pk FOREIGN KEY (hallgatoAzonosito) REFERENCES hallgato(azonosito)
);

CREATE TABLE kurzustfelvesz(
    hallgatoAzonosito VARCHAR2(6) not null,
    kurzusKod VARCHAR2(20) not null,
    teljesitette BOOLEAN default NO,
    CONSTRAINT kurzusHallgatoAzonosito_fk FOREIGN KEY (hallgatoAzonosito) REFERENCES hallgato(azonosito),
    CONSTRAINT kurzusKurzusKod_fk FOREIGN KEY (kurzusKod) REFERENCES kurzus(kurzuskod)
);

drop table kurzustfelvesz;
drop table vizsgazik;
drop table vizsga;
drop table idopont;
drop table kurzus;
drop table terem;
drop table osztondij;
drop table tartozasok;
drop table kezeloktatot;
drop table kezelhallgatot;
drop table hallgato;
drop table oktato;
drop table etradmin;
