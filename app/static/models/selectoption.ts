/**
 * Model for the items that go in a select element
 */
export class SelectOption {
   public key: string;
   public value: string;

   constructor(jsonObject: any) {
       this.key = jsonObject[0];
       this.value = jsonObject[1]
   }
}