import slate as st

with open("test.pdf") as f:
    doc = st.PDF(f)

    f = open("test.txt", "wt")
    for s in doc:
        f.write(s)

    f.close()
