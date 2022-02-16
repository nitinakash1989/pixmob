<template>
    <div class="vue-tempalte">
      <div class="container">
        <form>
            <h3>Sign In</h3>
            <div class="form-group">
                <label>Email address</label>
                <input v-model="addUserForm.email" type="email" class="form-control form-control-lg" />
            </div>
            <div class="form-group">
                <label>Password</label>
                <input v-model = "addUserForm.password" type="password" class="form-control form-control-lg" />
            </div>
            <button type="submit" class="btn btn-dark btn-lg btn-block" v-on:click="submitForm()">Sign In</button>
        </form>
      </div>
    </div>
</template>
<script>
import axios from 'axios';

export default {
  data() {
    return {
      addUserForm:{

        email: '',
        password: '',
      },
      ROOT_API: process.env.ROOT_API,
    }
  },
  methods:{
    submitForm() {

      const payload = {
        email: this.addUserForm.email,
        password: this.addUserForm.password
      };

      console.log("Submitting by form Nitin");
      const path = `${this.ROOT_API}/users`;
      axios.post(path, payload)
        .then(() => {
          if (!this.message){
            this.message = 'User added!';
          }
          console.log(this.message);
          
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    } 
  }
}
</script>