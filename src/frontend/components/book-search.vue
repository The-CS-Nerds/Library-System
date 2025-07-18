<template>
  <div class="book-search">
    <h1>Book Search</h1>

    <section class="form">
      <div class="field">
        <label>ISBN:</label>
        <input v-model="query.isbn" placeholder="e.g. 9780007158447" />
        <button @click="fetchBy('isbn')">Fetch by ISBN</button>
      </div>

      <div class="field">
        <label>Name:</label>
        <input v-model="query.name" placeholder="e.g. The Cat in the Hat" />
        <button @click="fetchBy('name')">Fetch by Name</button>
      </div>
    </section>

    <section v-if="error" class="error">
      {{ error }}
    </section>

    <section v-else-if="book" class="book-details">
      <h2>{{ book.title }}</h2>
      <p><strong>Author:</strong> {{ book.author }}</p>
      <p><strong>ISBN:</strong> {{ book.isbn }}</p>
      <p><strong>Description:</strong> {{ book.description }}</p>
    </section>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'BookSearch',
  data() {
    return {
      query: {
        id: '',
        isbn: '',
        name: ''
      },
      book: null,
      error: null
    }
  },
  methods: {
    async fetchBy(type) {
        this.book = null
        this.error = null
        let url = ''
        let params = {}

        if (type === 'id') {
        url    = 'http://localhost:8000/Book/getByID'
        params = { id: this.query.id }

        } else if (type === 'isbn') {
        url    = 'http://localhost:8000/Book/getByISBN'
        params = { isbn: this.query.isbn }

        } else if (type === 'name') {
        url    = 'http://localhost:8000/Book/getByName'
        params = { name: this.query.name }

        } else {
        throw new Error(`Unknown lookup type: ${type}`)
        }

      try {
        const res = await axios.get(url, { params })
        this.book = res.data
      } catch (err) {
        console.error(err)
        this.error = 'Could not fetch book'
      }
    }
  }
}
</script>

<style scoped>
/* This is css for the specific component, leave blank if using global styles */
</style>