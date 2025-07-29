from src.item import Item


class ChainItem:
    def __init__(self):
        self.head = None

    def add_bucket(self, bucket: Item):
        new_bucket = bucket
        if not self.head:
            self.head = new_bucket
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_bucket

    def get_bucket(self, key):
        head = self.head
        while head:
            if head.hash_object == hash(key):
                return head
            head = head.next
        return None

    def remove_link(self, key):
        current = self.head
        prev = None
        target_hash = hash(key)

        while current is not None:
            if current.hash_object == target_hash:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next

        return False

