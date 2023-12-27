from dataclasses import dataclass

from cloudengine import CloudProvider
from cloudengine.google import GoogleAuth

VIDEO_BUCKET = "video-backup.arjancodes.com"
REGION = "eu-west-1c"


@dataclass
class ACCloud:
    bucket_name: str
    cloud_provider: CloudProvider

    def find_files(self, query: str, max_result: int) -> str:
        response = self.cloud_provider.filter_by_query(
            bucket=self.bucket_name, query=query, max_val=max_result
        )
        return response["result"]["data"][0]


def build_cloud_provider(region: str = REGION, bucket: str = VIDEO_BUCKET) -> ACCloud:
    http_auth = GoogleAuth(key="service_key.json")
    secure = True

    cloud_provider = CloudProvider(region=region, http_auth=http_auth, secure=secure)
    return ACCloud(bucket_name=bucket, cloud_provider=cloud_provider)


def main():
    ac_cloud = build_cloud_provider()
    ac_cloud.find_files("some_query", 111)


if __name__ == "main":
    main()
