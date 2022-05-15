from typing import Text, List, Any, Dict
from rasa_sdk import Action, Tracker
from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet



class ValidateBSForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_bs_form"
    @staticmethod
    def bs_um_db() -> List[Text]:
        return ["meio=e+(d-ea)/2;","meio=e+(d-e)/2;"]
    
    @staticmethod
    def bs_dois_db() -> List[Text]:
        return ["return buscaBinaria(arr,meio+1,dir,x);","buscaBinaraaia(arr,meio+1,dir,x);"]
                
    def validate_bs_um(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
            if slot_value in self.bs_um_db():
                dispatcher.utter_message(text="Certo! Agora precisamos comparar o valor dentro da posição 'meio' com 'x', assim podemos desconsiderar metade da partição em que 'x' não poderá estar.")
                dispatcher.utter_message(text="Como você pode ver no código, já há uma condição if que verifica se 'x' vai se encontrar na metade inferior da partição, observe que uma chamada recursiva é feita,os seus paramêtros sinalizam que a função vai ser executada apenas tendo em conta somente os valores menores que 'arr[m]'")
                dispatcher.utter_message(text="Mas e a chamada recursão para se 'arr[m]' for menor que 'x'? Isso significa que 'x' tem que estar após 'arr[m]'. Seguindo nosso exemplo, observe na imagem como os paramêtros serão encontrados.")
                dispatcher.utter_message(image="https://i.imgur.com/hwb76nP.png")
                return {"bs_um": slot_value}
            else:
                dispatcher.utter_message(text="Tente de novo")
                return {"bs_um": None}

    def validate_bs_dois(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
            if slot_value in self.bs_dois_db():
                dispatcher.utter_message(text="Correto!")
                return {"bs_dois": slot_value}
            else:
                dispatcher.utter_message(text="Tente de novo")
                return {"bs_dois": None} 
        
            

class AskForBSUm(Action):
    def name(self) -> Text:
        return "action_ask_bs_um"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(text="Você consegue completar as variáveis na linha de código a seguir?")
        dispatcher.utter_message(image="https://i.imgur.com/LNye340.png")
        return []
    

class AskForBSDois(Action):
    def name(self) -> Text:
        return "action_ask_bs_dois"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:

        dispatcher.utter_message(text="Você consegue escrever os novos extremos da partição dentro da chamada recursiva?")
        dispatcher.utter_message(image="https://i.imgur.com/EXBLUrk.png")
        return []
    
                    
                            
class ValidateDFSForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_dfs_form"

    @staticmethod
    def dfs_um_db() -> List[Text]:
        return ["printEmOrdem(noaado->esq);","printEmOrdem(nodo->esq);"]
    @staticmethod
    def dfs_dois_db() -> List[Text]:
        return ['printf("%d",nodo->data);','printf("%d",nodo->data);']
    @staticmethod
    def dfs_tres_db() -> List[Text]:
        return ["printEmOrdeam(nodo->dir);","printEmOrdem(nodo->dir);"]
                
    def validate_dfs_um(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
            if slot_value in self.dfs_um_db():
                dispatcher.utter_message(text="Correto!")
                return {"dfs_um": slot_value}
            else:
                dispatcher.utter_message(text="Tente de novo")
                return {"dfs_um": None}

    def validate_dfs_dois(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
            if slot_value in self.dfs_dois_db():
                dispatcher.utter_message(text="Certo! Assim que não há mais nodos esquerdos, cada chamada recursiva segue sua execução. Porém, lembre que em Em-Ordem os nodos esquerdos mais profundos tem prioridade, logo antes de que cada nodo visite seu nodo-filho direito, o valor do nodo atual deve ser impresso.")
                dispatcher.utter_message(image="https://i.imgur.com/27V7VLr.png")
                dispatcher.utter_message(text="Por fim, nodos-filho direito deve ser então visitados e a mesma lógica que procura por nodos-filhos esquerdos é aplicada.")
                return {"dfs_dois": slot_value}
            else:
                dispatcher.utter_message(text="Tente de novo")
                return {"dfs_dois": None}

 
    def validate_dfs_tres(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
            if slot_value in self.dfs_tres_db():
                dispatcher.utter_message(text="Correto!")
                return {"dfs_tres": slot_value}
            else:
                dispatcher.utter_message(text="Tente de novo")
                return {"dfs_tres": None}           


            
        
            

class AskForDFSUm(Action):
    def name(self) -> Text:
        return "action_ask_dfs_um"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(text="Você consegue escrever a primeira recursão ma primeira linha incompleta?")
        return []
    

class AskForDFSDois(Action):
    def name(self) -> Text:
        return "action_ask_dfs_dois"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(text="Você consegue escrever a linha respectiva para aa impressão do valor?")
        return []

class AskForDFSTres(Action):
    def name(self) -> Text:
        return "action_ask_dfs_tres"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(text="Escreva a linha de código que acessa o nodo-filho direito.")
        dispatcher.utter_message(image="https://i.imgur.com/YELpjdo.png")
        return []    


                            
class ValidateQSForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_qs_form"

    @staticmethod
    def qs_um_db() -> List[Text]:
        return ["for(j=inf;j<=suaap-1;j++)","for(j=inf;j<=sup-1;j++)"]
    @staticmethod
    def qs_dois_db() -> List[Text]:
        return ["if(arr[j]<piaaavo)","if(arr[j]<pivo)"]
    @staticmethod
    def qs_tres_db() -> List[Text]:
        return ["swap(&arr[i],&arr[aaj]);","swap(&arr[i],&arr[j])"]
    @staticmethod
    def qs_quatro_db() -> List[Text]:
        return ["swap(&arr[sadi+1],&arr[sup];","swap(&arr[i+1],&arr[sup])"]
    @staticmethod
    def qs_cinco_db() -> List[Text]:
        return ["quickSort(arr,inf,pi-1);","quickSort(arr,inf,pi-1);"]
   
                
    def validate_qs_um(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
            if slot_value in self.qs_um_db():
                dispatcher.utter_message(text="Correto!")
                return {"qs_um": slot_value}
            else:
                dispatcher.utter_message(text="Tente de novo")
                return {"qs_um": None}

    def validate_qs_dois(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
            if slot_value in self.qs_dois_db():
                dispatcher.utter_message(text="Correto!")
                dispatcher.utter_message(text="Certo, a partir deste if vamos então colocar os elementos menores que o pivô na parte esquerda da partição utilizando a função swap.")

                return {"qs_dois": slot_value}
            else:
                dispatcher.utter_message(text="Tente de novo")
                return {"qs_dois": None}

            
    def validate_qs_tres(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
            if slot_value in self.qs_tres_db():
                dispatcher.utter_message(text="Correto!")
                return {"qs_tres": slot_value}
            else:
                dispatcher.utter_message(text="Tente de novo")
                return {"qs_tres": None} 
        

    def validate_qs_quatro(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
            if slot_value in self.qs_quatro_db():
                dispatcher.utter_message(text="Correto! Agora que temos o pivô anterior em seu lugar, devemos chamar a mesma função recursivamente para particionar e ordenar o espaço ao redor do pivô atual.")
                dispatcher.utter_message(image="https://i.imgur.com/7GOCtX8.png")
                return {"qs_quatro": slot_value}
            else:
                dispatcher.utter_message(text="Tente de novo")
                return {"qs_quatro": None}

    def validate_qs_cinco(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
            if slot_value in self.qs_cinco_db():
                dispatcher.utter_message(text="Correto!")
                return {"qs_cinco": slot_value}
            else:
                dispatcher.utter_message(text="Tente de novo")
                return {"qs_cinco": None}             
            

class AskForQSUm(Action):
    def name(self) -> Text:
        return "action_ask_qs_um"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(text="O primeiro passo é percorrer entre os extremos inferior e superior da partição ecomparar cada elemento com o pivô, complete a linha que implementa o 'for' que percorre os dois extremos da partição atual.")           
        dispatcher.utter_message(image="https://i.imgur.com/oNB9cGc.png")
        return []
    

class AskForQSDois(Action):
    def name(self) -> Text:
        return "action_ask_qs_dois"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(text="Ok! Agora você precisa comparar o valor do pivô com o elemento atual, neste exemplo, vamos verificar se o pivô é maior que o elemento atual.")
        dispatcher.utter_message(image="https://i.imgur.com/P7Dnbvu.png")
        return []

class AskForQSTres(Action):
    def name(self) -> Text:
        return "action_ask_qs_tres"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(text="Observe na imagem anterior que que ao incrementar um ao indexador i em cada swap podemos  indicar a parte da partição em que estes números menores que o pivô estão, dividindo a partição entre números menores e maiores durante a precursão da partição. Agora complete a função swap(), indicando as posições da partição que devem ser trocadas de lugar.")
        return []

class AskForQSQuatro(Action):
    def name(self) -> Text:
        return "action_ask_qs_quatro"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(text="Para encerrar a lógica de particionar a array, devemos colocar o pivô na sua posição correta na partição , já que esse se encontra atualmente na parte dos números maiores da partição, claro, este deve estar entre os números maiores e números menores que o próprio pivô.")
        dispatcher.utter_message(text="Vamos considerar que em nosso exemplo, a precursão da partição já ocorreu e colocamos os números maiores e menores que o pivô 70 em seus lados. Veja como agora o 70 deve ser colocado na posição i + 1, sendo arr[3] = 50, já que 50 foi o último número colocado naquele lado.")
        dispatcher.utter_message(image="https://i.imgur.com/mxKkRK3.png")
        dispatcher.utter_message(text="Lembre que você já sabe onde os números menores que o pivô terminam já que você tem o indexador i, agora, complete a função swap entre o elemento pivô e o elemento no limite de i.")
        return []

class AskForQSCinco(Action):
    def name(self) -> Text:
        return "action_ask_qs_cinco"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(text=" Escreva a linha de código que chama a recursão que vai particionar a parte da array anterior ao pivô atual, observe que a função partição de antes retorna o indexador do pivô, logo, a partição esquerda vai ser delimitada pelo extremo baixo atual e o elemento anterior ao pivô atual")
        dispatcher.utter_message(image="https://i.imgur.com/e7PZdiw.png")
        return []

class ResetBsUmSlot(Action):

    def name(self):
        return "action_reset_bs_um_slot"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("bs_um", None)]


class ResetBsDoisSlot(Action):

    def name(self):
        return "action_reset_bs_dois_slot"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("bs_dois", None)]

    
class ResetDFSUmSlot(Action):

    def name(self):
        return "action_reset_dfs_um_slot"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("dfs_um", None)]

        
class ResetDFSDoisSlot(Action):

    def name(self):
        return "action_reset_dfs_dois_slot"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("dfs_dois", None)]


                        
class ResetDFSTresSlot(Action):

    def name(self):
        return "action_reset_dfs_tres_slot"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("dfs_tres", None)]


class ResetQsUmSlot(Action):

    def name(self):
        return "action_reset_qs_um_slot"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("qs_um", None)]


class ResetQsDoisSlot(Action):

    def name(self):
        return "action_reset_qs_dois_slot"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("qs_dois", None)]


class ResetQsDTresSlot(Action):

    def name(self):
        return "action_reset_qs_tres_slot"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("qs_tres", None)]


class ResetQsQuatroSlot(Action):

    def name(self):
        return "action_reset_qs_quatro_slot"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("qs_quatro", None)]

class ResetQsCincoSlot(Action):

    def name(self):
        return "action_reset_qs_cinco_slot"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("qs_cinco", None)]
                        
                    
                    
