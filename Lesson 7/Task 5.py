#Task 5
system_telemetry = [
("srv_01", 12.5, 64, "online"),
("srv_02", 85.0, 92, "online"),
("srv_03", 0.0, 0, "offline"),
("srv_04", 45.2, 78, "online"),
("srv_05", 95.1, 99, "online")
]
node_name = [srv for srv, cpy, ram, status in system_telemetry if status == "online"]
cpy_load = [cpy for srv, cpy, ram, status in system_telemetry if status == "online"]
ram_usage = [ram for srv, cpy, ram, status in system_telemetry if status == "online"]
result = {'active_nodes_count': len(node_name), 'metrics': {
'average_cpu': sum(cpy_load)/len(cpy_load),
'max_ram': max(ram_usage)}
          }
print(f'Активные узлы в сети: {node_name}')
print(f'Итоговый отчет телеметрии: \n{result}')
