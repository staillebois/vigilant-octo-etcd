import etcd3


def main():
    etcd = etcd3.client()

    print(etcd.get('foo'))
    print(etcd.put('bar', 'doot'))
    print(etcd.get('bar'))
    print(etcd.delete('bar'))


if __name__ == '__main__':
    main()
