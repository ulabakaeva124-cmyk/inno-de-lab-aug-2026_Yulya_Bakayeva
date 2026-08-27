#Task 2
raw_transactions = [i.strip().strip('""') for i in input().strip('[]').split(',')]
print(raw_transactions)
clear_transactions = [int(t.split(':')[1]) for t in raw_transactions if t.startswith("SUCCESS") and int(t.split(':')[1])>0]
print(f'Очищенные транзакции: {clear_transactions}')


