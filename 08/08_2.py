import math

Vector = tuple[int, int, int]
Circuit = set[Vector]


def distance(p: Vector, q: Vector) -> float:
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 + (p[2] - q[2]) ** 2)


def find_circuits_containing_any(circuits: list[Circuit], vectors: set[Vector]) -> set[Circuit]:
    result = []

    for circuit in circuits:
        for vector in vectors:
            if vector in circuit and circuit not in result:
                result.append(circuit)
    return result


def circuit_contains_all(circuit: Circuit, vectors: list[Vector]) -> bool:
    for v in vectors:
        if v not in circuit:
            return False
    return True


with open("input.txt", "r") as file:
    lines = [l.strip() for l in file.readlines()]
    vectors = [(int(l.split(",")[0]), int(l.split(",")[1]), int(l.split(",")[2])) for l in lines]

distances = []

for i in range(len(vectors)):
    for j in range(i + 1, len(vectors)):
        distances.append((set([vectors[i], vectors[j]]), distance(vectors[i], vectors[j])))

distances.sort(key=lambda d: d[1])

circuits = []
i = 0

while len(circuits) == 0 or not circuit_contains_all(circuits[0], vectors):
    pair = distances[i][0]
    existing_circuits = find_circuits_containing_any(circuits, pair)

    if len(existing_circuits) == 0:
        circuits.append(set(pair))
    else:
        new_circuit = set()
        for c in existing_circuits:
            new_circuit = new_circuit | c | pair
            circuits.remove(c)
        circuits.append(new_circuit)
    i += 1

pair = list(pair)
print(pair[0][0] * pair[1][0])