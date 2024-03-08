from chain.chains import ThesisSummaryChain


def main():
    chain = ThesisSummaryChain()
    chain.invoke()


if __name__ == "__main__":
    main()
