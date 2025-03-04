import io
import json
import pickle

from configs.config import MINIO_ACCESS_KEY, MINIO_ENDPOINT, MINIO_SECRET_KEY
from minio import Minio


def get_minio_client():
    return Minio(
        endpoint=MINIO_ENDPOINT,
        access_key=MINIO_ACCESS_KEY,
        secret_key=MINIO_SECRET_KEY,
        secure=False,
    )


def create_bucket(minio_client, bucket_name):
    try:
        if not minio_client.bucket_exists(bucket_name):
            minio_client.make_bucket(bucket_name=bucket_name)
            print(f"Bucket '{bucket_name}' created.")
        else:
            print(f"Bucket '{bucket_name}' already exists.")
    except Exception as e:
        print(f"Error creating bucket '{bucket_name}': {e}")


def load_pkl_data_from_minio(minio_client, file_name, bucket_name):
    try:
        response = minio_client.get_object(
            bucket_name=bucket_name, object_name=file_name
        )

        return pickle.loads(response.data)
    except Exception as e:
        print(f"Error loading {file_name} from MinIO: {e}")
        return {}


def save_pkl_data_to_minio(minio_client, file_name, data, bucket_name):
    try:
        bytes_data = io.BytesIO(pickle.dumps(data))

        minio_client.put_object(
            bucket_name=bucket_name,
            object_name=file_name,
            data=bytes_data,
            length=len(bytes_data.getvalue()),
        )
    except Exception as e:
        print(f"Error saving {file_name} to MinIO: {e}")


def save_json_data_to_minio(minio_client, file_name, data, bucket_name):
    try:
        bytes_data = io.BytesIO(json.dumps(data).encode("utf-8"))

        minio_client.put_object(
            bucket_name=bucket_name,
            object_name=file_name,
            data=bytes_data,
            length=len(bytes_data.getvalue()),
        )
    except Exception as e:
        print(f"Error saving {file_name} to MinIO: {e}")


def load_json_data_from_minio(minio_client, file_name, bucket_name):
    try:
        response = minio_client.get_object(
            bucket_name=bucket_name, object_name=file_name
        )

        return json.loads(response.data)
    except Exception as e:
        print(f"Error loading {file_name} from MinIO: {e}")
        return {}
