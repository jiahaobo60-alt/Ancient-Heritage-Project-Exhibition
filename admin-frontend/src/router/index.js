import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import BuildingList from '../views/BuildingList.vue'
import DynastyList from '../views/DynastyList.vue'
import RegionList from '../views/RegionList.vue'
import ProvinceStats from '../views/ProvinceStats.vue'
import ElementList from '../views/ElementList.vue'
import LiteratureList from '../views/LiteratureList.vue'
import UserList from '../views/UserList.vue'

const routes = [
  { path: '/', redirect: '/dashboard' },
  { path: '/dashboard', name: 'Dashboard', component: Dashboard },
  { path: '/buildings', name: 'BuildingList', component: BuildingList },
  { path: '/dynasties', name: 'DynastyList', component: DynastyList },
  { path: '/regions', name: 'RegionList', component: RegionList },
  { path: '/provinces', name: 'ProvinceStats', component: ProvinceStats },
  { path: '/elements', name: 'ElementList', component: ElementList },
  { path: '/literatures', name: 'LiteratureList', component: LiteratureList },
  { path: '/users', name: 'UserList', component: UserList },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
