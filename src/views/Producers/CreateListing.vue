<!-- HTML -->
<template>
    <!-- navbar-->
<NavBar />
<SubmitListingNew mode = "power" />
    <!-- collapsible content -->
    


</template>

<!-- ---------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<!-- CSS -->

<!-- ---------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<!-- JavaScript -->
<script>
    // import axios from 'axios'
    import NavBar from '@/components/NavBar.vue'
    import SubmitListingNew from '@/components/SubmitListingNew.vue'
    export default {
        components:{
            NavBar,
            SubmitListingNew
        },
    // data() {
    //     return {
    //     responseCode:"",
    //     isOperator: false,
    //     fillForm: true,
    //     submitForm: false,
    //     successCreation: false,
    //     errorCreation: false,
    //     duplicateEntry:false,
    //     errorMessage:false,
    //     form:{
    //         "Expression Name": "",
    //         "Producer": "",
    //         "Bottler (OB or Specify name of IB)": "",
    //         "Country of Origin": "",
    //         "Drink Type": "",
    //         "Drink Category": "",
    //         "Age": "",
    //         "ABV": "",
    //         "88B Website Review (if applicable)": "",
    //         "Official Description": "",
    //     },
    //     };
    // },
    // methods: {
        // checkRadio(){
        //     if(this.isOperator){
        //         this.form['Bottler (OB or Specify name of IB)'] = ""
        //     }
        // },

        // // Method to send post request, upon button click, hide the form, then display the results

        // async createListing(){
        //     // form validation first
        //     this.fillForm=false;
        //     this.submitForm=true;
        //     let alertPhrase = "";
        //     if(this.isOperator){
        //         this.form["Bottler (OB or Specify name of IB)"] = "OB"
        //     }
        //     if (!this.form["Expression Name"].trim()){
        //         alertPhrase += "Name of bottle is needed.\n"
        //     }
        //     if(!this.form["Drink Type"].trim()){
        //         alertPhrase += "Type of drink is needed.\n"
        //     }
        //     if(!this.form["88B Website Review (if applicable)"].trim()){
        //         alertPhrase += "Link to website or source is needed.\n"
        //     }
        //     if(!this.form["Bottler (OB or Specify name of IB)"].trim()){
        //         alertPhrase += "Name of bottler is needed.\n"
        //     }
        //     if(alertPhrase){
        //         alert(alertPhrase)
        //         return "error"
        //     }


        //     const response = await this.$axios.post('http://127.0.0.1:5001/createListings',this.form)
        //     .then((response)=>{
        //         this.responseCode = response.data.code
        //     })
        //     .catch((error)=>{
        //         console.log(error);
        //         this.responseCode = error.response.data.code
        //     });
        //     console.log(this.responseCode)
        //     if(this.responseCode==201){
        //         this.successCreation=true;
        //         this.submitForm=false;
        //     }else{
        //         this.errorCreation=true;
        //         this.submitForm=false;
        //         if(this.responseCode==400){
        //             this.duplicateEntry = true
        //         }else{
        //             this.errorMessage = true
        //         }
        //     }
        //     return response

        // },

        // reset(){
        //     this.fillForm=true
        //     this.successCreation=false
        //     this.submitForm=false
        //     this.errorCreation= false
        //     this.duplicateEntry= false
            
        //     this.responseCode= ""
        //     this.isOperator = false
        //     for (const key in this.form) {
        //         this.form[key] = "";
        //     }
        // },

    // }
    };
    
</script>


