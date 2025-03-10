# LANACO PMF praksa 2025

OneDrive link sa prezentacijama:
https://1drv.ms/f/c/9155c25dfb5cad28/EoRd0DXe1oRFv0XMf_3PCZoBoPTWZ2zKbg06K4p7_2vVZw?e=55rfjo

**Tema**: _Sistem za real-time preporuku bankarskih proizvoda_

## Opis sistema
Sistem za preporuke bankarskih proizvoda koristi real-time podatke za generisanje preporuka za klijente. Sistem se sastoji od nekoliko ključnih komponenti:
- Generator podataka (stream-data)
- Priprema podataka za treniranje (prepare-data)
- Treniranje modela (train-model)
- Real-time predikcije (inference)

## Arhitektura
- **Redpanda**: Message broker za real-time podatke - koristi se za prenos podataka između generatora podataka i baze podataka.
- **PostgreSQL**: Baza podataka
- **RisingWave**: Stream processing engine - koristi se za obradu podataka u realnom vremenu.   
- **MinIO**: Object storage - koristi se za skladištenje skupova podataka, istreniranih modela, osim toga koristi se kao *temp cache* prilikom generisanja preporuka.   
- **Grafana**: Vizualizacija podataka i preporuka - koristi se za prikazivanje rezultata i praćenje performansi sistema.  


## Pristup servisima
- **RisingWave**: http://localhost:5691/ - root:root
- **MinIO**: http://localhost:9001/ - minioadmin:minioadmin
- **Redpanda**: http://localhost:8080/ 
- **Grafana**: http://localhost:3000/ - grafana:grafana

Za pristup bazi koristiti DBeaver sa sljedećim podacima:
- **Host**: localhost
- **Port**: 4566
- **Database**: dev
- **User**: root
- **Password**: root

Za pristup RisingWave-u putem Grafane, za source izabrati PostgreSQL, za parametre koristiti:
- **Host**: host.docker.internal
- **Port**: 4566
- **Database**: dev
- **User**: root
- **Password**: root


## Napomene
- Za pokretanje sistema, potrebno je kreirati `.env` fajl sa potrebnim konfiguracionim parametrima i sačuvati ga u `main/configs` direktorijumu. Sadržaj `.env` fajla:
```bash
# RisingWave
RISINGWAVE_HOST=localhost
RISINGWAVE_PORT=4566
RISINGWAVE_DB=dev
RISINGWAVE_USER=root
RISINGWAVE_PASSWORD=root

# Redpanda
KAFKA_BROKER=localhost:19092

# MinIO
MINIO_ENDPOINT=localhost:9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin
MINIO_TRAIN_DATA_BUCKET=train-data
MINIO_TRAINED_MODEL_BUCKET=trained-models
MINIO_CACHE_BUCKET=cache
```
- Potrebno je instalirati sve potrebne biblioteke iz `docker/requirements.txt` fajla
- Prvo je potrebno podići infrastrukturu, a zatim pokrenutati skripte
- Za podešavanje konfiguracija, koristiti konfiguracione fajlove u `main/configs` direktorijumu
- Prilikom dodavanja source-a u Grafani, koristiti `host.docker.internal:port` za pristup RisingWave-u
- **Važno** Kada se pokrene Docker Desktop, potrebno je prebaciti se na WSL (Linux) engine, ako nije već podešeno.
