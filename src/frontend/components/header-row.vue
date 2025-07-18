<template>
  <header class="header-row">
    <!-- Left side: app navigation -->
    <nav class="nav-left">
      <router-link to="/books" class="nav-item">Books</router-link>
      <router-link to="/loans" class="nav-item">Current Loans</router-link>
      <router-link to="/dashboard" class="nav-item">Dashboard</router-link>
    </nav>
    <div class="nav-right">
      <router-link to="/login" class="login-button">
        Login
      </router-link>
    </div>
  </header>
</template>
<script>
export default {
  name: 'HeaderRow'
}
</script>

<style scoped>
/* This is css for the specific component, leave blank if using global styles */
</style>