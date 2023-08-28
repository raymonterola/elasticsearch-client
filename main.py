from elasticsearch import Elasticsearch

ELASTIC_USERNAME = "elastic"
ELASTIC_PASSWORD = "A4GXYsvXFO_M9V3HE*m*"
ELASTIC_PATH = "https://localhost:9200"
INDEX_NAME = "nba_players"

mapping = {
    "properties": {
        "first_name": {"type": "text"},
        "last_name": {"type": "text"},
        "date_of_birth": {"type": "date"},
        "position": {"type": "keyword"},
        "team": {"type": "keyword"},
        "avg_scoring": {"type": "float"},
        "avg_rebound": {"type": "float"},
        "avg_assist": {"type": "float"},
        "country": {"type": "keyword"},
    }
}


def create_index(es):
    es.indices.create(index=INDEX_NAME, mappings=mapping)


def create_client():
    client = Elasticsearch(
        ELASTIC_PATH,
        verify_certs=True,
        basic_auth=(ELASTIC_USERNAME, ELASTIC_PASSWORD),
        ca_certs="http_ca.crt",
    )
    return client


def main():
    es = create_client()
    create_index(es)


if __name__ == "__main__":
    main()
