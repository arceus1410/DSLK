#include <iostream>
using namespace std;

class Node{
public:
    int stt;
    Node* next;	
};

Node* createNode(int _stt){
    Node* p = new Node;
    p->stt = _stt;
    p->next = NULL;
    return p;
}

int main(){
    cout << "enter number of players : " ;
    int n; cin >> n;

//create n players
    Node* first_player = new Node; first_player->stt = 1; // create 1st player
    Node* last_player = createNode(n); //create the last player
    last_player->next = first_player;  

    Node* temp = new Node;
    for(int i = 2; i <= n; i++){
        if(i == 2 ){
            temp = createNode(i);
            first_player->next = temp;
        }else{
            if( i == n ){
                temp->next = last_player;  //complete the circle
                temp = temp->next; 
            }else{
                temp->next = createNode(i);
                temp = temp->next;
            }

        }
    }temp= temp->next; // move temp to first_player

// rule
    int m; cout << "Enter the number of steps in each round : " ; cin >> m; 
    
    if(m == 0){ 
        cout << "Eliminated players : "; 
        n = n - 1;
        while(n--){
            if(n == 0 ) cout << temp->stt << endl ;
            else cout << temp -> stt << " , " ;
            temp = temp -> next;
        }
        cout << "The winner is player number " << last_player->stt << endl;
    }else{
        cout << "Eliminated players : "; 
        while(n > 2){
            int check = m-1 ;
            if(check == 0){
                cout <<  temp->next->stt << " , " ;
                temp->next = temp->next->next;  
                temp = temp->next; 
                n--;
            }else {
                while(check -- ){
                    temp = temp->next;       
                }
                cout <<  temp->next->stt << " , ";
                temp->next = temp->next->next; 
                temp = temp->next;   
                n --;
            }
            
        }
        while(m--){
            temp = temp->next;
        }
        cout << temp->stt << endl;
        cout << "The winner is player number " << temp->next->stt << endl;
    }
}