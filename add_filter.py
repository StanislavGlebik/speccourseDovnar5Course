<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>147</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <widget class="QDialogButtonBox" name="buttonBox">
   <property name="geometry">
    <rect>
     <x>40</x>
     <y>110</y>
     <width>341</width>
     <height>32</height>
    </rect>
   </property>
   <property name="orientation">
    <enum>Qt::Horizontal</enum>
   </property>
   <property name="standardButtons">
    <set>QDialogButtonBox::Cancel|QDialogButtonBox::Ok</set>
   </property>
  </widget>
  <widget class="QWidget" name="">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>10</y>
     <width>361</width>
     <height>91</height>
    </rect>
   </property>
   <layout class="QFormLayout" name="formLayout">
    <item row="0" column="0">
     <widget class="QLabel" name="label">
      <property name="text">
       <string>Dimension</string>
      </property>
     </widget>
    </item>
    <item row="0" column="1">
     <widget class="QComboBox" name="chooseDimension"/>
    </item>
    <item row="1" column="0">
     <widget class="QLabel" name="label_2">
      <property name="text">
       <string>Sign</string>
      </property>
     </widget>
    </item>
    <item row="1" column="1">
     <widget class="QComboBox" name="chooseSign"/>
    </item>
    <item row="2" column="0">
     <widget class="QLabel" name="label_3">
      <property name="text">
       <string>Value</string>
      </property>
     </widget>
    </item>
    <item row="2" column="1">
     <widget class="QComboBox" name="chooseValue"/>
    </item>
   </layout>
  </widget>
 </widget>
 <resources/>
 <connections>
  <connection>
   <sender>buttonBox</sender>
   <signal>accepted()</signal>
   <receiver>Dialog</receiver>
   <slot>accept()</slot>
   <hints>
    <hint type="sourcelabel">
     <x>248</x>
     <y>254</y>
    </hint>
    <hint type="destinationlabel">
     <x>157</x>
     <y>274</y>
    </hint>
   </hints>
  </connection>
  <connection>
   <sender>buttonBox</sender>
   <signal>rejected()</signal>
   <receiver>Dialog</receiver>
   <slot>reject()</slot>
   <hints>
    <hint type="sourcelabel">
     <x>316</x>
     <y>260</y>
    </hint>
    <hint type="destinationlabel">
     <x>286</x>
     <y>274</y>
    </hint>
   </hints>
  </connection>
 </connections>
</ui>
