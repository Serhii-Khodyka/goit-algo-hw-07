class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        self.replies.append(reply)

    def remove_reply(self, target_reply):
        for reply in self.replies:
            if reply == target_reply:
                reply.text = "Цей коментар було видалено."
                reply.is_deleted = True
                return True
        return False

    def display(self, depth=0):
        indent = "    " * depth
        if not self.is_deleted:
            print(f"{indent}{self.author}: {self.text}")
        else:
            print(f"{indent}Цей коментар було видалено.")
        
        for reply in self.replies:
            reply.display(depth + 1)

# Приклад використання
root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

# видаляємо коментар reply1
root_comment.remove_reply(reply1)

root_comment.display()
