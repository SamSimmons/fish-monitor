<template lang="html">
  <div class="tank-list__create">
    <div class="name"><span>Create New Tank</span> <icon name="plus"></icon></div>
    <div class="create-form">
      <div class="create-form__field create-form__field--long">
        <label for="tank-name">Name:</label>
        <input type="text" name="tank-name" v-model="name" v-validate="'required'" />
        <div class="create-form__error" v-show="errors.has('tank-name')">{{ errors.first('tank-name') }}</div>
      </div>
      <div class="create-form__field create-form__field--long">
        <label for="tank-water-change">Last water change:</label>
        <datepicker v-model="lastWaterChange"></datepicker>
      </div>
      <div class="create-form__field">
        <label for="tank-frequency">Water change frequency: (days)</label>
        <input class="num" type="text" name="tank-frequency" v-model="changeFrequency" v-validate="'numeric'" />
        <div class="create-form__error" v-show="errors.has('tank-frequency')">{{ errors.first('tank-frequency') }}</div>
      </div>
      <div class="create-form__field">
        <label for="tank-temperature">Temperature: (°c)</label>
        <input class="num" type="text" name="tank-temperature" v-model="temperature" v-validate="'numeric'" />
        <div class="create-form__error" v-show="errors.has('tank-tank-temperature')">{{ errors.first('tank-tank-temperature') }}</div>
      </div>
      <div class="create-form__field">
        <label for="tank-ph">pH level:</label>
        <input class="num" type="text" name="tank-ph" v-model="ph" v-validate="'decimal'" />
        <div class="create-form__error" v-show="errors.has('tank-ph')">{{ errors.first('tank-ph') }}</div>
      </div>
      <div class="create-form__field">
        <label for="tank-ammonia">Ammonia level:</label>
        <input class="num" type="text" name="tank-ammonia" v-model="ammonia" v-validate="'decimal'" />
        <div class="create-form__error" v-show="errors.has('tank-ammonia')">{{ errors.first('tank-ammonia') }}</div>
      </div>
      <button class="btn btn--white create-form__submit" v-on:click="submitNewTank">Go</button>
    </div>
  </div>
</template>

<script>
import Icon from 'vue-awesome/components/Icon'
import Datepicker from 'vuejs-datepicker'
import Auth from './Auth'
import axios from 'axios'

export default {
  components: {
    Icon,
    Datepicker
  },
  data () {
    return {
      name: '',
      lastWaterChange: '',
      changeFrequency: '',
      temperature: '0',
      ph: '0.00',
      ammonia: '0.00'
    }
  },
  methods: {
    submitNewTank () {
      const { name, lastWaterChange, changeFrequency, temperature, ph, ammonia } = this
      if (name === '') {
        this.errors.add('tank-name', 'The tank-name field is required.')
        return
      }
      const formattedData = {
        'last_water_change': lastWaterChange.getTime(),
        'name': name
      }
      if (changeFrequency !== '') {
        formattedData['water_change_freq'] = changeFrequency
      }
      if (temperature !== '0') {
        formattedData['last_temp'] = temperature
      }
      if (ph !== '0.00') {
        formattedData['last_ph'] = ph
      }
      if (ammonia !== '0.00') {
        formattedData['last_ammonia'] = ammonia
      }
      const headers = { Authorization: `Token ${Auth.getToken()}` }
      axios({
        method: 'post',
        url: 'http://localhost:8000/tanks/',
        headers,
        data: formattedData
      })
        .then((res) => {
          this.$emit('update-list')
          this.name = ''
          this.lastWaterChange = ''
          this.changeFrequency = ''
          this.temperature = '0'
          this.ph = '0.00'
          this.ammonia = '0.00'
        })
        .catch((err) => {
          console.log(err.response)
        })
    }
  },
  created () {
    this.lastWaterChange = new Date()
  }
}
</script>

<style lang="css">

.tank-list__create {
  background: var(--primary);
  color: var(--white);
  display: flex;
  flex-flow: row wrap;
  margin-top: 30px;
  padding: 30px;
}

.tank-list__create .name {
  align-items: center;
  border-left: 5px solid var(--white);
  color: var(--white);
  display: flex;
  justify-content: space-between;
  flex: 1 1 100%;
  font-size: 1.4rem;
  font-weight: 700;
  margin-left: -30px;
  padding-left: 25px;
}

.tank-list__create svg {
  height: 30px;
  width: 30px;
}

.create-form { flex: 0 1 500px; }

.create-form__field {
  display: flex;
  justify-content: space-between;
  flex-flow: row wrap;
  margin-top: 7px;
}

.create-form__field input {
  background: var(--primary);
  border: 0;
  border-bottom: 1px solid var(--white);
  flex: 0 1 60px;
  min-width: 0;
  text-align: right;
}

.create-form__field--long input { flex: 0 1 180px; }

.vdp-datepicker input { width: 180px; }

.create-form__submit {
  margin-top: 10px;
}

.create-form__error {
  color: var(--error);
  flex: 0 1 100%;
  font-size: .8rem;
  text-align: right;
}

.vdp-datepicker__calendar {
  color: var(--primary);
}

.vdp-datepicker__calendar header .prev::after { border-right: 10px solid var(--primary) !important; }
.vdp-datepicker__calendar header .next::after {border-left: 10px solid var(--primary) !important; }
.vdp-datepicker__calendar { right: 0; }

.vdp-datepicker__calendar .cell.selected,
.vdp-datepicker__calendar .cell.selected.highlighted,
.vdp-datepicker__calendar .cell.selected:hover {
  background: var(--primary) !important;
  color: var(--white);
}

.vdp-datepicker__calendar .cell:not(.blank):not(.disabled).day:hover,
.vdp-datepicker__calendar .cell:not(.blank):not(.disabled).month:hover,
.vdp-datepicker__calendar .cell:not(.blank):not(.disabled).year:hover {
  border: 1px solid var(--primary) !important;
}

</style>
