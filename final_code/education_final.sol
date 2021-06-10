pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";




contract government_coin is ERC721Full  {
    address payable owner;
    address public government_account;
    //string dropout_course;
    
    constructor() public ERC721Full ("EDU", "$$") { 
        government_account = msg.sender; // government agency
        owner = msg.sender; // government agency
        
        balance[government_account] = gov_initial_supply;
    }  // Government to Student

        
        event record (address student_name, uint balance_event , string student_name1);
        
        mapping (address => uint) public balance;
        mapping (address => string) public names;
        
        string  token_name = "EDU" ;
        string  tokenSymbol = "$$";
        uint gov_initial_supply = 200;
        
       
        
        function student_name (address student_address, string memory name) public
        {
            names[student_address] = name;
        }
        
     
     
        function transfer (address student, uint token_transfer) public 
        {
            balance[student] = balance[student]+ token_transfer; 
            
            balance[government_account] = balance[government_account] - token_transfer;
            
            emit record ( student, balance[student] , names[student]);
            
        }
        
        
        function balances (address _account) public view returns (uint) 
        {
            //balance = address(this).balance ;
            
            return balance[_account];
        }
        
        function main_balances () public view returns (uint) 
        {
            //balance = address(this).balance ;

            
            return balance[owner];
        }

        
        // function _burn(address owner, uint256 tokenId ) internal
        // {
        // require(ownerOf(tokenId) == owner, "ERC721: burn of token that is not own");
        // emit Transfer(owner, address(0), tokenId);
        
        // }
        
        
      function() external payable
      {   }
      
       }
       
       
  
      
      
      
    