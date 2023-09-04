<template>
  
  <v-app id="inspire">
    <v-navigation-drawer
      hide-overlay
      fixed
      temporary
      :mini-variant.sync="mini"

      :value="true"
      :clipped="$vuetify.breakpoint.mdAndUp"
      :disable-resize-watcher="true"
      app
      v-model="drawer"
    >
      <v-list dense>
        <template v-for="item in items">
          <v-layout
            row
            v-if="item.heading"
            align-center
            :key="item.heading"
          >
            <v-flex xs6>
              <v-subheader v-if="item.heading">
                {{ item.heading }}
              </v-subheader>
            </v-flex>
            <v-flex xs6 class="text-xs-center">
              <a href="#!" class="body-2 black--text">EDIT</a>
            </v-flex>
          </v-layout>
      
          <v-list-tile v-else @click="" :key="item.text">
            <v-list-tile-action>
              
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-tile-action>
            
            <v-list-tile-content>
              <v-list-tile-title>
                <router-link class="nav" :to="'/easeheart'">{{ item.text }}</router-link>
              </v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </template>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar
      color="blue darken-3"
      dark
      app
      :clipped-left="$vuetify.breakpoint.mdAndUp"
      fixed
    >
      <v-toolbar-title style="width: 300px" class="ml-0 pl-3">
        <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
        <span ><router-link class="index" :to="'/'">Guan Ling</router-link></span>
      </v-toolbar-title>
      <v-text-field
        flat
        solo-inverted
        prepend-icon="search"
        label="Search"
        class="hidden-sm-and-down"
      ></v-text-field>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>apps</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>notifications</v-icon>
      </v-btn>

    </v-toolbar>
    <v-content class="content">
      <v-container  >
        <!-- <v-layout justify-center align-center> -->
            <router-view></router-view>

        <!-- </v-layout> -->
        
      </v-container>
      
    </v-content>
    <v-footer height="auto" class="bo blue darken-3">
        <v-layout row wrap justify-center>
          <!-- <v-btn
            color="white"
            flat
            v-for="link in links"
            :key="link"
          >
            {{ link }}
          </v-btn> -->
          <v-flex xs12 py-3 text-xs-center white--text>
            &copy;2016 — 2018 <strong>psyguanling.com</strong>
          </v-flex>
        </v-layout>
      </v-footer> 
  </v-app>
</template>

<script>
    export default {
        name:"Layouts",
        data: () => ({
          mini: true,
      dialog: false,
      drawer: null,
      items: [
        { icon: 'history', text: '静心' },
       
      ]
    }),
    props: {
      source: String
    }
    }
</script>

<style scoped>
.index {
  text-decoration: none;
  color: #ffffff;
}
.nav {
  text-decoration: none;
  color: #000000;
}
.bo {
  bottom: 0;
}
.content {
  min-height: 1000px;
}
</style>
