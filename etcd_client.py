import etcd3
import uuid


def main(etcd_):
    etcd_key = str(uuid.uuid1())

    etcd_.put(etcd_key, etcd_key)
    print(f'PUT {etcd_key}')
    etcd_.put(etcd_key, etcd_key)
    print(f'PUT update {etcd_key}')
    etcd_.put(etcd_key, etcd_key)
    print(f'PUT update {etcd_key}')
    etcd_.put(etcd_key, etcd_key)
    print(f'PUT update {etcd_key}')


if __name__ == '__main__':
    etcd = etcd3.client()
    while True:
        main(etcd)