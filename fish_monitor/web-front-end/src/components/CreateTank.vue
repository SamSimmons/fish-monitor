<template lang="html">
  <div class="tank-list__create">
    <div class="name"><span>Create New Tank</span> <icon name="plus"></icon></div>
  </div>
</template>

<script>
import Icon from 'vue-awesome/components/Icon'

export default {
  components: {
    Icon
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

</style>
