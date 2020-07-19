<template>
  <nav id="sandbox">
    <v-navigation-drawer
      v-model="primaryDrawer.drawer"
      :color="primaryDrawer.color"
      :permanent="primaryDrawer.permanent"
      :mini-variant="primaryDrawer.mini"
      :expand-on-hover="primaryDrawer.hover"
      app
      overflow
    >
      <v-list dense nav class="py-0">
        <v-list-item two-line :class="miniVariant && 'px-0'">
          <v-list-item-avatar>
            <img src="https://randomuser.me/api/portraits/men/81.jpg" />
          </v-list-item-avatar>

          <v-list-item-content>
            <v-list-item-title>Application</v-list-item-title>
            <v-list-item-subtitle>Subtext</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>

        <v-divider></v-divider>

        <v-list-item v-for="item in items" :key="item.title" router :to="item.route">
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar flat app>
      <v-app-bar-nav-icon @click="primaryDrawer.mini = !primaryDrawer.mini" class="grey--text"></v-app-bar-nav-icon>
      <v-toolbar-title class="text-h4 grey--text">
        <span class="font-weight-light">Kafka</span>
        <span>Stream</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>

      <v-btn small flat color="grey">
        <span>Sign Out</span>
        <v-icon right>mdi-exit-to-app</v-icon>
      </v-btn>
    </v-toolbar>
  </nav>
</template>

<script>
export default {
  data: () => ({
    items: [
      { title: "BusMaps", icon: "mdi-view-dashboard", route: "/" },
      { title: "Tweet Updates", icon: "mdi-help-box", route: "/" }
    ],
    primaryDrawer: {
      drawer: true,
      permanent: true,
      mini: true,
      color: "success",
      hover: false
    }
  })
};
</script>

<style></style>
