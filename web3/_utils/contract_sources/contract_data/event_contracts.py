"""
Generated by `compile_contracts.py` script.
Compiled with Solidity v0.8.28.
"""

# source: web3/_utils/contract_sources/EventContracts.sol:EventContract
EVENT_CONTRACT_BYTECODE = "0x6080604052348015600e575f5ffd5b5061017a8061001c5f395ff3fe608060405234801561000f575f5ffd5b5060043610610029575f3560e01c80635818fad71461002d575b5f5ffd5b610047600480360381019061004291906100f1565b610049565b005b7ff70fe689e290d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb1581604051610078919061012b565b60405180910390a17f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d4816040516100af919061012b565b60405180910390a150565b5f5ffd5b5f819050919050565b6100d0816100be565b81146100da575f5ffd5b50565b5f813590506100eb816100c7565b92915050565b5f60208284031215610106576101056100ba565b5b5f610113848285016100dd565b91505092915050565b610125816100be565b82525050565b5f60208201905061013e5f83018461011c565b9291505056fea2646970667358221220ffb25fdd3a92ed8f87f68da4885d8c0f5e6fd2edeafb3d1cab0da0f2683b846b64736f6c634300081c0033"  # noqa: E501
EVENT_CONTRACT_RUNTIME = "0x608060405234801561000f575f5ffd5b5060043610610029575f3560e01c80635818fad71461002d575b5f5ffd5b610047600480360381019061004291906100f1565b610049565b005b7ff70fe689e290d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb1581604051610078919061012b565b60405180910390a17f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d4816040516100af919061012b565b60405180910390a150565b5f5ffd5b5f819050919050565b6100d0816100be565b81146100da575f5ffd5b50565b5f813590506100eb816100c7565b92915050565b5f60208284031215610106576101056100ba565b5b5f610113848285016100dd565b91505092915050565b610125816100be565b82525050565b5f60208201905061013e5f83018461011c565b9291505056fea2646970667358221220ffb25fdd3a92ed8f87f68da4885d8c0f5e6fd2edeafb3d1cab0da0f2683b846b64736f6c634300081c0033"  # noqa: E501
EVENT_CONTRACT_ABI = [
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "arg0",
                "type": "uint256",
            }
        ],
        "name": "LogSingleArg",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "arg0",
                "type": "uint256",
            }
        ],
        "name": "LogSingleWithIndex",
        "type": "event",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_arg0", "type": "uint256"}],
        "name": "logTwoEvents",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]
EVENT_CONTRACT_DATA = {
    "bytecode": EVENT_CONTRACT_BYTECODE,
    "bytecode_runtime": EVENT_CONTRACT_RUNTIME,
    "abi": EVENT_CONTRACT_ABI,
}


# source: web3/_utils/contract_sources/EventContracts.sol:IndexedEventContract
INDEXED_EVENT_CONTRACT_BYTECODE = "0x6080604052348015600e575f5ffd5b506101708061001c5f395ff3fe608060405234801561000f575f5ffd5b5060043610610029575f3560e01c80635818fad71461002d575b5f5ffd5b610047600480360381019061004291906100e7565b610049565b005b807ff70fe689e290d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb1560405160405180910390a27f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d4816040516100a59190610121565b60405180910390a150565b5f5ffd5b5f819050919050565b6100c6816100b4565b81146100d0575f5ffd5b50565b5f813590506100e1816100bd565b92915050565b5f602082840312156100fc576100fb6100b0565b5b5f610109848285016100d3565b91505092915050565b61011b816100b4565b82525050565b5f6020820190506101345f830184610112565b9291505056fea2646970667358221220c54729ba3e926e84d8497888e2dc66bd33efa5e4ebcd95e323dc53eb183500cc64736f6c634300081c0033"  # noqa: E501
INDEXED_EVENT_CONTRACT_RUNTIME = "0x608060405234801561000f575f5ffd5b5060043610610029575f3560e01c80635818fad71461002d575b5f5ffd5b610047600480360381019061004291906100e7565b610049565b005b807ff70fe689e290d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb1560405160405180910390a27f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d4816040516100a59190610121565b60405180910390a150565b5f5ffd5b5f819050919050565b6100c6816100b4565b81146100d0575f5ffd5b50565b5f813590506100e1816100bd565b92915050565b5f602082840312156100fc576100fb6100b0565b5b5f610109848285016100d3565b91505092915050565b61011b816100b4565b82525050565b5f6020820190506101345f830184610112565b9291505056fea2646970667358221220c54729ba3e926e84d8497888e2dc66bd33efa5e4ebcd95e323dc53eb183500cc64736f6c634300081c0033"  # noqa: E501
INDEXED_EVENT_CONTRACT_ABI = [
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "arg0",
                "type": "uint256",
            }
        ],
        "name": "LogSingleArg",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "arg0",
                "type": "uint256",
            }
        ],
        "name": "LogSingleWithIndex",
        "type": "event",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_arg0", "type": "uint256"}],
        "name": "logTwoEvents",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]
INDEXED_EVENT_CONTRACT_DATA = {
    "bytecode": INDEXED_EVENT_CONTRACT_BYTECODE,
    "bytecode_runtime": INDEXED_EVENT_CONTRACT_RUNTIME,
    "abi": INDEXED_EVENT_CONTRACT_ABI,
}
