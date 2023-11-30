def main():
    entrada = list(map(lambda x: list(map(int, x.split(":"))), input().split()))

    h1, m1 = entrada[0][0], entrada[0][1]
    h2, m2 = entrada[1][0], entrada[1][1]
    h3, m3 = entrada[2][0], entrada[2][1]
    h4, m4 = entrada[3][0], entrada[3][1]

    t1, t2, t3, t4 = h1 * 60 + m1, h2 * 60 + m2, h3 * 60 + m3, h4 * 60 + m4

    d1 = 1440 - t1 + t2 if t1 > t2 else t2 - t1
    d2 = 1440 - t3 + t4 if t3 > t4 else t4 - t3

    voo_hr = (d1 + d2) // 2 - (720 if d1 + d2 > 1440 else 0)
    fus_diferent = d1 - voo_hr - (1440 if d1 - voo_hr > 720 else 0)

    print(f"{voo_hr} {fus_diferent // 60}")

if __name__ == "__main__":
    main()
