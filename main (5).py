from eth_account.messages import encode_defunct
from web3.middleware import geth_poa_middleware
from pyuseragents import random as random_ua
from termcolor import cprint
from requests import Session
from ctypes import windll
from web3 import Web3
from tqdm import tqdm
import random
import time

from settings import *


web3 = Web3(Web3.HTTPProvider('https://rpc.ankr.com/bsc'))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)
web3_polygon = Web3(Web3.HTTPProvider('https://rpc.ankr.com/polygon'))
web3_polygon.middleware_onion.inject(geth_poa_middleware, layer=0)

nft_abi = '[{"inputs":[{"internalType":"uint256","name":"_mintStartTime","type":"uint256"},{"internalType":"uint256","name":"_mintEndTime","type":"uint256"},{"internalType":"uint256","name":"_mintLimit","type":"uint256"},{"internalType":"string","name":"_metadataUri","type":"string"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"ApprovalCallerNotOwnerNorApproved","type":"error"},{"inputs":[],"name":"ApprovalQueryForNonexistentToken","type":"error"},{"inputs":[],"name":"ApproveToCaller","type":"error"},{"inputs":[],"name":"BalanceQueryForZeroAddress","type":"error"},{"inputs":[],"name":"InvalidQueryRange","type":"error"},{"inputs":[],"name":"MintERC2309QuantityExceedsLimit","type":"error"},{"inputs":[],"name":"MintToZeroAddress","type":"error"},{"inputs":[],"name":"MintZeroQuantity","type":"error"},{"inputs":[],"name":"OwnerQueryForNonexistentToken","type":"error"},{"inputs":[],"name":"OwnershipNotInitializedForExtraData","type":"error"},{"inputs":[],"name":"TransferCallerNotOwnerNorApproved","type":"error"},{"inputs":[],"name":"TransferFromIncorrectOwner","type":"error"},{"inputs":[],"name":"TransferToNonERC721ReceiverImplementer","type":"error"},{"inputs":[],"name":"TransferToZeroAddress","type":"error"},{"inputs":[],"name":"URIQueryForNonexistentToken","type":"error"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"fromTokenId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"toTokenId","type":"uint256"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"ConsecutiveTransfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"explicitOwnershipOf","outputs":[{"components":[{"internalType":"address","name":"addr","type":"address"},{"internalType":"uint64","name":"startTimestamp","type":"uint64"},{"internalType":"bool","name":"burned","type":"bool"},{"internalType":"uint24","name":"extraData","type":"uint24"}],"internalType":"struct IERC721A.TokenOwnership","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"tokenIds","type":"uint256[]"}],"name":"explicitOwnershipsOf","outputs":[{"components":[{"internalType":"address","name":"addr","type":"address"},{"internalType":"uint64","name":"startTimestamp","type":"uint64"},{"internalType":"bool","name":"burned","type":"bool"},{"internalType":"uint24","name":"extraData","type":"uint24"}],"internalType":"struct IERC721A.TokenOwnership[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"userAddress","type":"address"}],"name":"getMintSurplus","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"mintEndTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"mintLimit","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"mintStartTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_mintStartTime","type":"uint256"},{"internalType":"uint256","name":"_mintEndTime","type":"uint256"}],"name":"setMintTimes","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"tokensOfOwner","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"start","type":"uint256"},{"internalType":"uint256","name":"stop","type":"uint256"}],"name":"tokensOfOwnerIn","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
nft_address = web3.to_checksum_address('0x40a2A882c82AD7cC74E5f58Cde7612c07956D4A6')
contract = web3.eth.contract(address=nft_address, abi=nft_abi)

bridge_abi = '[{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"previousAdmin","type":"address"},{"indexed":false,"internalType":"address","name":"newAdmin","type":"address"}],"name":"AdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"beacon","type":"address"}],"name":"BeaconUpgraded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"oldContract","type":"address"},{"indexed":true,"internalType":"address","name":"newContract","type":"address"}],"name":"ContractUpgraded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"pendingImplementation","type":"address"},{"indexed":true,"internalType":"address","name":"newImplementation","type":"address"}],"name":"NewPendingImplementation","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint64","name":"sequence","type":"uint64"},{"indexed":false,"internalType":"address","name":"sourceToken","type":"address"},{"indexed":false,"internalType":"address","name":"token","type":"address"},{"indexed":false,"internalType":"uint256","name":"tokenID","type":"uint256"},{"indexed":false,"internalType":"uint16","name":"sourceChain","type":"uint16"},{"indexed":false,"internalType":"uint16","name":"sendChain","type":"uint16"},{"indexed":false,"internalType":"address","name":"recipient","type":"address"}],"name":"ReceiveNFT","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"chainId","type":"uint16"},{"indexed":false,"internalType":"address","name":"nftBridge","type":"address"}],"name":"RegisterChain","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint64","name":"sequence","type":"uint64"},{"indexed":false,"internalType":"address","name":"token","type":"address"},{"indexed":false,"internalType":"uint256","name":"tokenID","type":"uint256"},{"indexed":false,"internalType":"uint16","name":"recipientChain","type":"uint16"},{"indexed":false,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"address","name":"recipient","type":"address"}],"name":"TransferNFT","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"implementation","type":"address"}],"name":"Upgraded","type":"event"},{"inputs":[],"name":"MIN_LOCK_TIME","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"chainId_","type":"uint16"}],"name":"bridgeContracts","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"chainId","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"confirmContractUpgrade","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"implementation","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"impl","type":"address"}],"name":"isInitialized","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"}],"name":"isWrappedAsset","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lockTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"bytes","name":"","type":"bytes"}],"name":"onERC721Received","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pendingImplementation","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"chainId","type":"uint16"},{"internalType":"address","name":"contractAddress","type":"address"}],"name":"registerChain","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"lockTime","type":"uint256"}],"name":"setLockTime","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newImplementation","type":"address"}],"name":"submitContractUpgrade","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"toUpdateTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"tokenImplementation","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"tokenID","type":"uint256"},{"internalType":"uint16","name":"recipientChain","type":"uint16"},{"internalType":"bytes32","name":"recipient","type":"bytes32"}],"name":"transferNFT","outputs":[{"internalType":"uint64","name":"sequence","type":"uint64"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address[]","name":"tokenList","type":"address[]"},{"internalType":"uint256[]","name":"tokenIDList","type":"uint256[]"},{"internalType":"uint16","name":"recipientChain","type":"uint16"},{"internalType":"bytes32","name":"recipient","type":"bytes32"}],"name":"transferNFTBatch","outputs":[{"internalType":"uint64","name":"sequence","type":"uint64"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint16","name":"tokenChainId","type":"uint16"},{"internalType":"bytes32","name":"tokenAddress","type":"bytes32"}],"name":"wrappedAsset","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"zkBridge","outputs":[{"internalType":"contract IZKBridge","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"srcChainId","type":"uint16"},{"internalType":"address","name":"srcAddress","type":"address"},{"internalType":"uint64","name":"sequence","type":"uint64"},{"internalType":"bytes","name":"payload","type":"bytes"}],"name":"zkReceive","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
bridge_address = web3.to_checksum_address('0xE09828f0DA805523878Be66EA2a70240d312001e')
brigde_contract = web3.eth.contract(address=bridge_address, abi=bridge_abi)

receive_abi = '[{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"previousAdmin","type":"address"},{"indexed":false,"internalType":"address","name":"newAdmin","type":"address"}],"name":"AdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"beacon","type":"address"}],"name":"BeaconUpgraded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"oldContract","type":"address"},{"indexed":true,"internalType":"address","name":"newContract","type":"address"}],"name":"ContractUpgraded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"uint16","name":"srcChainId","type":"uint16"},{"indexed":true,"internalType":"uint64","name":"sequence","type":"uint64"},{"indexed":false,"internalType":"address","name":"dstAddress","type":"address"},{"indexed":false,"internalType":"bytes","name":"payload","type":"bytes"}],"name":"ExecutedMessage","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"uint16","name":"dstChainId","type":"uint16"},{"indexed":true,"internalType":"uint64","name":"sequence","type":"uint64"},{"indexed":false,"internalType":"address","name":"dstAddress","type":"address"},{"indexed":false,"internalType":"bytes","name":"payload","type":"bytes"}],"name":"MessagePublished","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"pendingImplementation","type":"address"},{"indexed":true,"internalType":"address","name":"newImplementation","type":"address"}],"name":"NewPendingImplementation","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"implementation","type":"address"}],"name":"Upgraded","type":"event"},{"stateMutability":"payable","type":"fallback"},{"inputs":[],"name":"MESSAGE_TOPIC","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MIN_LOCK_TIME","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"chainId","type":"uint16"}],"name":"blockUpdater","outputs":[{"internalType":"contract IBlockUpdater","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"chainId","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"confirmContractUpgrade","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"impl","type":"address"}],"name":"isInitialized","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"hash","type":"bytes32"}],"name":"isTransferCompleted","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lockTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"chainId","type":"uint16"}],"name":"mptVerifier","outputs":[{"internalType":"contract IMptVerifier","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"hash","type":"bytes32"}],"name":"nextSequence","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pendingImplementation","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"chainId","type":"uint16"},{"internalType":"bytes32","name":"bridgeContract","type":"bytes32"}],"name":"registerChain","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"dstChainId","type":"uint16"},{"internalType":"address","name":"dstAddress","type":"address"},{"internalType":"bytes","name":"payload","type":"bytes"}],"name":"send","outputs":[{"internalType":"uint64","name":"sequence","type":"uint64"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint16","name":"chainId","type":"uint16"},{"internalType":"address","name":"blockUpdater","type":"address"}],"name":"setBlockUpdater","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"lockTime","type":"uint256"}],"name":"setLockTime","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"chainId","type":"uint16"},{"internalType":"address","name":"mptVerifier","type":"address"}],"name":"setMptVerifier","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newImplementation","type":"address"}],"name":"submitContractUpgrade","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"toUpdateTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"srcChainId","type":"uint16"},{"internalType":"bytes32","name":"srcBlockHash","type":"bytes32"},{"internalType":"uint256","name":"logIndex","type":"uint256"},{"internalType":"bytes","name":"mptProof","type":"bytes"}],"name":"validateTransactionProof","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"chainId","type":"uint16"}],"name":"zkBridgeContracts","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]'
receive_address =  web3.to_checksum_address('0xa25be50be65070c2ad96d5ed639061de31c45e12')
receive_contract = web3_polygon.eth.contract(address=receive_address, abi=receive_abi)

testnet_msg_abi = '[{"inputs":[{"internalType":"address","name":"_zkBridgeEntrypoint","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint64","name":"sequence","type":"uint64"},{"indexed":true,"internalType":"uint32","name":"dstChainId","type":"uint32"},{"indexed":true,"internalType":"address","name":"dstAddress","type":"address"},{"indexed":false,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"address","name":"recipient","type":"address"},{"indexed":false,"internalType":"string","name":"message","type":"string"}],"name":"MessageSend","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"inputs":[],"name":"claimFees","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"fee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"dstChainId","type":"uint16"},{"internalType":"address","name":"dstAddress","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"string","name":"message","type":"string"}],"name":"sendMessage","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_fee","type":"uint256"}],"name":"setFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_maxLength","type":"uint256"}],"name":"setMsgLength","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"zkBridgeEntrypoint","outputs":[{"internalType":"contract IZKBridgeEntrypoint","name":"","type":"address"}],"stateMutability":"view","type":"function"}]'
testnet_msg_address = web3.to_checksum_address('0x044332f4b34fD5639482dE41cD1d767F7304fA00')
testnet_msg_contract = web3.eth.contract(address=testnet_msg_address, abi=testnet_msg_abi)

direct_msg_abi = '[{"inputs":[{"internalType":"address","name":"zkBridgeEntrypointAddress","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint64","name":"sequence","type":"uint64"},{"indexed":true,"internalType":"uint32","name":"dstChainId","type":"uint32"},{"indexed":true,"internalType":"address","name":"dstAddress","type":"address"},{"indexed":false,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"address","name":"recipient","type":"address"},{"indexed":false,"internalType":"string","name":"message","type":"string"}],"name":"MessageSend","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"inputs":[],"name":"claimFees","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"fee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"dstChainId","type":"uint16"},{"internalType":"address","name":"dstAddress","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"string","name":"message","type":"string"}],"name":"sendMessage","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_fee","type":"uint256"}],"name":"setFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"zkBridgeEntrypoint","outputs":[{"internalType":"contract IZKBridgeEntrypoint","name":"","type":"address"}],"stateMutability":"view","type":"function"}]'
direct_msg_address = web3.to_checksum_address('0x5c5979832A60c17bB06676fa906bEdD1A013e18c')
direct_msg_contract = web3.eth.contract(address=direct_msg_address, abi=direct_msg_abi)


def sleeping(from_sleep, to_sleep):
    x = random.randint(from_sleep, to_sleep)
    for _ in tqdm(range(x), desc='sleep ', bar_format='{desc}: {n_fmt}/{total_fmt}'):
        time.sleep(1)

def get_bearer(pk, session):
    retry = 0
    while True:
        try:
            address = web3.eth.account.from_key(pk).address

            r = session.post('https://api.zkbridge.com/api/signin/validation_message', json={"publicKey": address.lower()})
            if r.status_code not in [200,201] or r.json().get('message') == None:
                cprint(f'bad validation request: {r.status_code} {r.reason}: {r.text}, trying again...', 'yellow')
                sleeping(15, 15)
                continue

            message = r.json()['message']
            encoded_msg = encode_defunct(text=message)
            signed_message = web3.eth.account.sign_message(encoded_msg, pk)

            payload = {
                "publicKey": address.lower(),
                "signedMessage": signed_message.signature.hex()
            }
            r = session.post('https://api.zkbridge.com/api/signin', json=payload)
            if r.status_code not in [200,201] or r.json().get('token') == None:
                cprint(f'bad signin request: {r.status_code} {r.reason}: {r.text}, trying again...', 'yellow')
                sleeping(15, 15)
                continue
            cprint(f'Successfully logged in', 'cyan')
            return r.json()['token']
        except Exception as err:
            retry += 1
            cprint(f'get bearer error: {type(err).__name__} {err}', 'red')
            if retry < RETRY:
                cprint(f'[{retry}/{RETRY}] trying again...', 'yellow')
                sleeping(15, 15)
            else:
                return False

def mint(pk):
    retry = 0
    while True:
        try:
            address = web3.eth.account.from_key(pk).address
            mint_tx = contract.functions.mint().build_transaction({
                'from': address,
                'gasPrice': random.randint(MIN_GWEI, MAX_GWEI),
                'nonce': web3.eth.get_transaction_count(address)
            })
            mint_tx['gas'] = int(web3.eth.estimate_gas(mint_tx) * 1.2)
            signed_tx = web3.eth.account.sign_transaction(mint_tx, pk)
            tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            cprint(f"Mint tx sent: https://bscscan.com/tx/{tx_hash.hex()}")
            status = web3.eth.wait_for_transaction_receipt(tx_hash, timeout=360).status
            if status != 1:
                raise ValueError(f'bad tx status: {status}')
            else:
                cprint('Successfully minted!', 'green')

                topics = web3.eth.get_transaction_receipt(tx_hash)['logs'][0]['topics']
                nft_num = topics[-1].hex()
                return int(nft_num, 16)

        except Exception as err:
            retry += 1
            cprint(f'mint error: {type(err).__name__} {err}', 'red')
            if retry < RETRY:
                cprint(f'[{retry}/{RETRY}] trying again...', 'yellow')
                sleeping(15, 15)
            else: return False

def approve_nft(pk, nft_num):
    retry = 0
    while True:
        try:
            address = web3.eth.account.from_key(pk).address
            approve_tx = contract.functions.approve(web3.to_checksum_address('0xe09828f0da805523878be66ea2a70240d312001e'), nft_num).build_transaction({
                'from': address,
                'gasPrice': random.randint(MIN_GWEI, MAX_GWEI),
                'nonce': web3.eth.get_transaction_count(address)
            })

            approve_tx['gas'] = int(web3.eth.estimate_gas(approve_tx) * 1.2)
            signed_tx = web3.eth.account.sign_transaction(approve_tx, pk)
            tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            cprint(f"Approve tx sent: https://bscscan.com/tx/{tx_hash.hex()}")
            status = web3.eth.wait_for_transaction_receipt(tx_hash, timeout=360).status
            if status != 1:
                raise ValueError(f'bad tx status: {status}')
            else:
                cprint('Successfully approved NFT!', 'green')
                return True
        except Exception as err:
            retry += 1
            cprint(f'approve error: {type(err).__name__} {err}', 'red')
            if retry < RETRY+5:
                cprint(f'[{retry}/{RETRY+5}] trying again...', 'yellow')
                sleeping(15, 15)
            else: return False

def transfer_nft(pk, nft_num):
    retry = 0
    while True:
        try:
            address = web3.eth.account.from_key(pk).address

            transfer_tx = brigde_contract.functions.transferNFT(
                nft_address,
                nft_num,
                4, # 4 - polygon; 5 - avax; 6 - ftm
                '0x'+address.lower()[2:].rjust(64, '0')
            ).build_transaction({
                'from': address,
                'gasPrice': random.randint(MIN_GWEI, MAX_GWEI),
                'nonce': web3.eth.get_transaction_count(address),
                'value': int(0.001 * 10 ** 18)
            })

            transfer_tx['gas'] = int(web3.eth.estimate_gas(transfer_tx) * 1.2)
            signed_tx = web3.eth.account.sign_transaction(transfer_tx, pk)
            tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            cprint(f"Transfer tx sent: https://bscscan.com/tx/{tx_hash.hex()}")
            status = web3.eth.wait_for_transaction_receipt(tx_hash, timeout=360).status
            if status != 1:
                raise ValueError(f'bad tx status: {status}')
            else:
                cprint('Successfully transferred!', 'green')

                return tx_hash.hex()

        except Exception as err:
            retry += 1
            cprint(f'mint error: {type(err).__name__} {err}', 'red')
            if retry < RETRY:
                cprint(f'[{retry}/{RETRY}] trying again...', 'yellow')
                sleeping(15, 15)
            else: return False

def receive_nft(pk, tx_hash, session):
    retry = 0
    while True:
        try:
            address = web3.eth.account.from_key(pk).address

            payload = {
                "tx_hash": tx_hash,
                "chain_id": 3,
                "testnet": False
            }
            r = session.post('https://api.zkbridge.com/api/v2/receipt_proof/generate', json=payload)
            if r.status_code not in [200,201]:
                cprint(f'bad request: {r.status_code} {r.reason}: {r.text}, trying again...', 'yellow')
                sleeping(15, 15)
                continue


            receive_tx = receive_contract.functions.validateTransactionProof(
                r.json()['chain_id'],
                r.json()['block_hash'],
                r.json()['proof_index'],
                r.json()['proof_blob'],
            ).build_transaction({
                'from': address,
                'gasPrice': web3_polygon.eth.gas_price,
                'nonce': web3_polygon.eth.get_transaction_count(address),
            })

            receive_tx['gas'] = int(web3_polygon.eth.estimate_gas(receive_tx) * 1.2)
            signed_tx = web3_polygon.eth.account.sign_transaction(receive_tx, pk)
            tx_hash = web3_polygon.eth.send_raw_transaction(signed_tx.rawTransaction)
            cprint(f"Receive tx sent: https://polygonscan.com/tx/{tx_hash.hex()}")

            status = web3_polygon.eth.wait_for_transaction_receipt(tx_hash, timeout=360).status
            if status != 1:
                raise ValueError(f'bad tx status: {status}')
            else:
                cprint('Successfully received!', 'green')
                return tx_hash.hex()

        except Exception as err:
            retry += 1
            cprint(f'mint error: {type(err).__name__} {err}', 'red')
            if retry < RETRY:
                cprint(f'[{retry}/{RETRY}] trying again...', 'yellow')
                sleeping(15, 15)
            else: return False

def abuse_polyhedra_nft(pk):
    address = web3.eth.account.from_key(pk).address
    cprint(f'\n\n[{address}] started', 'cyan')

    with Session() as session:
        session.headers['user-agent'] = random_ua()
        bearer = get_bearer(pk, session)
        if not bearer: return False
        session.headers['authorization'] = f'Bearer {bearer}'
        sleeping(MIN_SLEEP_BETWEEN, MAX_SLEEP_BETWEEN)

        nft_num = mint(pk)
        if not nft_num: return False
        sleeping(MIN_SLEEP_BETWEEN, MAX_SLEEP_BETWEEN)

        if not approve_nft(pk, nft_num): return False
        sleeping(MIN_SLEEP_BETWEEN, MAX_SLEEP_BETWEEN)

        tx_hash = transfer_nft(pk, nft_num)
        if not tx_hash: return False
        sleeping(MIN_SLEEP_BETWEEN, MAX_SLEEP_BETWEEN)

        tx_hash = receive_nft(pk, tx_hash, session)
        if not tx_hash: return False

        try:
            payload = {
                "claimHash": tx_hash,
                "id": "000000000000000000000000"
            }
            r = session.post('https://api.zkbridge.com/api/bridge/claimOrder', json=payload)

            timed_color = 'green' if r.status_code == 200 else 'yellow'

            cprint(f'Claim order status: {r.status_code} {r.reason}', timed_color)
        except Exception as err:
            cprint(f'Claim order error: {type(err).__name__} {err}', 'yellow')


def abuse_polyhedra_msg(pk):
    address = web3.eth.account.from_key(pk).address
    cprint(f'\n\n[{address}] started', 'cyan')

    with Session() as session:
        session.headers['user-agent'] = random_ua()
        bearer = get_bearer(pk, session)
        if not bearer: return False
        session.headers['authorization'] = f'Bearer {bearer}'
        sleeping(MIN_SLEEP_BETWEEN, MAX_SLEEP_BETWEEN)

        repeat_count = random.randint(MIN_MSG_COUNT, MAX_MSG_COUNT)
        for i in range(repeat_count):
            send_msg(pk, session)

            if i != repeat_count - 1:
                sleeping(MIN_SLEEP_BETWEEN, MAX_SLEEP_BETWEEN)

def send_msg(pk, session):
    retry = 0
    while True:
        try:
            address = web3.eth.account.from_key(pk).address

            last_block = web3_polygon.eth.get_block(web3_polygon.eth.block_number - random.randint(5,30))
            random_address = web3_polygon.eth.get_transaction(random.choice(last_block['transactions']))['from']

            if MSG_METHOD == 'BNB Greenfield testnet':
                msg_contract = testnet_msg_contract
                value = int(0.0005 * 10 ** 18)
                confirm_url = 'https://api.zkbridge.com/api/gf/msg'

                payload = {'text': "<div style=\"text-align:center\"><strong>Releasing Greenfield zkMessenger 📧</strong></div><br/><u>Polyhedra Network </u>is delighted to release Greenfield zkMessenger 📧, the first cross-chain data availability protocol powered by <u>BNB Greenfield</u> and <u>zkBridge.</u>🌈<br/><br/>With Greenfield zkMessenger, you can send Web3 emails across multiple blockchain networks, just as convenient as Internet emails. Your data is protected by <u>BNB Greenfield</u> and <u>zkBridge.</u><br/><br/>We would like to express our gratitude for the community's support.<u> Polyhedra Network </u>remains committed to launching innovative products and enhancing user experience.🎉"}
                r = session.post('https://gfapi.zkbridge.com/v1/saveMessage', json=payload)
                if r.status_code not in [200,201] or r.json().get('data') == None:
                    cprint(f'bad take message request: {r.status_code} {r.reason}: {r.text}, trying again...', 'yellow')
                    sleeping(15, 15)
                    continue
                if 'Cannot create an object on BNB Greenfield testnet' in r.json().get('msg'):
                    cprint(f'Cannot create a message object, trying again... | You can switch `MSG_METHOD` in settings.py', 'yellow')
                    time.sleep(2)
                    continue
                uri = r.json()['data']['uri']
            elif MSG_METHOD == 'Direct Message':
                msg_contract = direct_msg_contract
                uri = 'Embrace the future of cross-chain interoperability on zkBridge! 🌈'
                value = int(0.0008 * 10 ** 18)
                confirm_url = 'https://api.zkbridge.com/api/msg'
            else:
                cprint(f'No method with name "{MSG_METHOD}"', 'red')
                return False

            mailSenderAddress = msg_contract.address
            msg_tx = msg_contract.functions.sendMessage(
                4, # to_chain | polygon - 4 | combo - 114
                random_address,
                address,
                uri
            ).build_transaction({
                'from': address,
                'gasPrice': random.randint(MIN_GWEI, MAX_GWEI),
                'nonce': web3.eth.get_transaction_count(address),
                'value': value
            })

            msg_tx['gas'] = int(web3.eth.estimate_gas(msg_tx) * 1.2)
            signed_tx = web3.eth.account.sign_transaction(msg_tx, pk)
            tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            cprint(f"Tx with message sent: https://bscscan.com/tx/{tx_hash.hex()}")
            status = web3.eth.wait_for_transaction_receipt(tx_hash, timeout=360).status
            if status != 1:
                raise ValueError(f'bad message tx status: {status}')

            logs = web3.eth.get_transaction_receipt(tx_hash)['logs']
            sequence = int(logs[0]['topics'][-1].hex(), 16)

            payload = {
                "mailSenderAddress": mailSenderAddress,
                "receiverAddress": random_address,
                "receiverChainId": 4,
                "sendTimestamp": int(time.time()),
                "senderAddress": address,
                "senderChainId": 3,
                "senderTxHash": tx_hash.hex(),
                "sequence": sequence
            }
            if uri == 'Embrace the future of cross-chain interoperability on zkBridge! 🌈':
                payload['message'] = uri
            else:
                payload['uri'] = uri


            r = session.post(confirm_url, json=payload)

            if r.status_code not in [200, 201]:
                cprint(f'bad confirm message request: {r.status_code} {r.reason}: {r.text}, trying again...', 'yellow')
                sleeping(15, 15)
                continue
            else:
                cprint('Message successfully sent!', 'green')
                return True
        except Exception as err:
            retry += 1
            cprint(f'send msg error: {type(err).__name__} {err}', 'red')
            if retry < RETRY:
                cprint(f'[{retry}/{RETRY}] trying again...', 'yellow')
                sleeping(15,15)
            else:
                return False


if __name__ == '__main__':
    windll.kernel32.SetConsoleTitleW(f'Polyhedra bot')

    with open('private_keys.txt') as f:
        p_keys = f.read().splitlines()

    random.shuffle(p_keys)
    counter = 0

    cprint(f'\nWhat function you want?\n1. Claim & transfer Loyalty Program NFT\n2. Send messages', 'cyan')
    want_func = input()

    if want_func == '1': poly_func = abuse_polyhedra_nft
    elif want_func == '2': poly_func = abuse_polyhedra_msg

    if want_func in ['1', '2']:
        for pk in p_keys:
            try:
                counter += 1
                windll.kernel32.SetConsoleTitleW(f'Polyhedra bot [{counter}/{len(p_keys)}]')

                poly_func(pk)
            except Exception as err:
                cprint(f'main error: {type(err).__name__} {err}', 'red')
            sleeping(MIN_SLEEP_AFTER_ACC, MAX_SLEEP_AFTER_ACC)
    else: cprint(f'No function with id {want_func}', 'red')


    cprint(f'\n\npress Enter to exit', 'cyan')
    input()
