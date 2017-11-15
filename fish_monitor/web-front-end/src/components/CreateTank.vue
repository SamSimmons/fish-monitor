<template lang="html">
  <div class="tank-list__create">
    <div class="name"><span>Create New Tank</span> <icon name="plus"></icon></div>
    <div class="ceate-form">
      <div class="create-form__field">
        <label for="tank-name">Name:</label>
        <input type="text" name="tank-name" v-model="name" />
      </div>
      <div class="create-form__field">
        <label for="tank-water-change">Last water change:</label>
        <!-- <input type="datetime-local" name="tank-water-change" v-model="lastWaterChange" /> -->
        <datepicker></datepicker>
      </div>
      <div class="create-form__field">
        <label for="tank-frequency">Water change frequency</label>
        <input class="num" type="number" name="tank-frequency" v-model="changeFrequency" />
      </div>
      <div class="create-form__field">
        <label for="tank-temperature">Temperature:</label>
        <input class="num" type="number" name="tank-temperature" v-model="temperature" />
      </div>
      <div class="create-form__field">
        <label for="tank-ph">pH level:</label>
        <input class="num" type="number" name="tank-ph" v-model="ph" />
      </div>
      <div class="create-form__field">
        <label for="tank-ammonia">Ammonia level:</label>
        <input class="num" type="number" name="tank-ammonia" v-model="ammonia" />
      </div>
      <button class="btn btn--white create-form__submit">Go</button>
    </div>
  </div>
</template>

<script>
import Icon from 'vue-awesome/components/Icon'
import Datepicker from 'vuejs-datepicker'

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
  }
}
</script>

<style lang="css">

.tank-list__create {
  background: var(--primary);
  color: var(--white);
  margin-top: 30px;
  padding: 30px;
}

.tank-list__create .name {
  align-items: center;
  border-left: 5px solid var(--white);
  color: var(--white);
  display: flex;
  justify-content: space-between;
  font-size: 1.4rem;
  font-weight: 700;
  margin-left: -30px;
  padding-left: 25px;
}

.tank-list__create svg {
  height: 30px;
  width: 30px;
}

.create-form__field {
  display: flex;
  justify-content: space-between;
}

.create-form__field .num {
  flex: 0 1 60px;
}

.create-form__field input {
  background: var(--primary);
  border: 0;
  border-bottom: 1px solid var(--white);
}

.create-form__submit {
  margin-top: 10px;
}

.vdp-datepicker__calendar {
  color: var(--primary);
}


.vdp-datepicker__calendar header .prev::after {
  border-right: var(--primary);
}

</style>
